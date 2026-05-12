/**
 * Email Spam Detection - Frontend JavaScript
 * Handles theme toggling, animations, and UI interactions
 */

// ===================================
// Theme Management
// ===================================

function initTheme() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
    
    // Add transition effect
    document.body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
}

function updateThemeIcon(theme) {
    const themeToggle = document.querySelector('.theme-toggle');
    if (themeToggle) {
        themeToggle.textContent = theme === 'light' ? '🌙' : '☀️';
    }
}

// ===================================
// Smooth Scrolling
// ===================================

function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ===================================
// Animations on Scroll
// ===================================

function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe cards and feature items
    document.querySelectorAll('.card, .feature-card, .stat-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// ===================================
// Form Validation
// ===================================

function validateMessage(message) {
    if (!message || message.trim().length === 0) {
        return {
            valid: false,
            error: 'Please enter a message to check'
        };
    }
    
    if (message.trim().length < 10) {
        return {
            valid: false,
            error: 'Message is too short. Please enter at least 10 characters.'
        };
    }
    
    if (message.length > 5000) {
        return {
            valid: false,
            error: 'Message is too long. Maximum 5000 characters allowed.'
        };
    }
    
    return { valid: true };
}

// ===================================
// Notification System
// ===================================

function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existing = document.querySelector('.notification');
    if (existing) {
        existing.remove();
    }
    
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <span>${message}</span>
        <button onclick="this.parentElement.remove()">×</button>
    `;
    
    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 80px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'success' ? 'var(--success-color)' : 
                     type === 'error' ? 'var(--danger-color)' : 
                     'var(--primary-color)'};
        color: white;
        border-radius: 10px;
        box-shadow: var(--shadow-lg);
        z-index: 9999;
        display: flex;
        align-items: center;
        gap: 1rem;
        animation: slideIn 0.3s ease;
    `;
    
    const closeBtn = notification.querySelector('button');
    closeBtn.style.cssText = `
        background: none;
        border: none;
        color: white;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 0;
        width: 24px;
        height: 24px;
        display: flex;
        align-items: center;
        justify-content: center;
    `;
    
    document.body.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentElement) {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }
    }, 5000);
}

// Add animation keyframes
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// ===================================
// Character Counter
// ===================================

function initCharacterCounter() {
    const textarea = document.getElementById('messageInput');
    if (!textarea) return;
    
    const counter = document.createElement('div');
    counter.className = 'character-counter';
    counter.style.cssText = `
        text-align: right;
        font-size: 0.875rem;
        color: var(--text-secondary);
        margin-top: 0.5rem;
    `;
    
    textarea.parentElement.insertBefore(counter, textarea.nextSibling);
    
    function updateCounter() {
        const length = textarea.value.length;
        const maxLength = 5000;
        counter.textContent = `${length} / ${maxLength} characters`;
        
        if (length > maxLength) {
            counter.style.color = 'var(--danger-color)';
        } else if (length > maxLength * 0.9) {
            counter.style.color = 'var(--warning-color)';
        } else {
            counter.style.color = 'var(--text-secondary)';
        }
    }
    
    textarea.addEventListener('input', updateCounter);
    updateCounter();
}

// ===================================
// Keyboard Shortcuts
// ===================================

function initKeyboardShortcuts() {
    document.addEventListener('keydown', (e) => {
        // Ctrl/Cmd + Enter to submit
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            const checkButton = document.querySelector('button[onclick="checkSpam()"]');
            if (checkButton) {
                checkButton.click();
            }
        }
        
        // Ctrl/Cmd + K to clear
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            const clearButton = document.querySelector('button[onclick="clearInput()"]');
            if (clearButton) {
                clearButton.click();
            }
        }
        
        // Ctrl/Cmd + L to load sample
        if ((e.ctrlKey || e.metaKey) && e.key === 'l') {
            e.preventDefault();
            const sampleButton = document.querySelector('button[onclick="loadSample()"]');
            if (sampleButton) {
                sampleButton.click();
            }
        }
    });
}

// ===================================
// Copy to Clipboard
// ===================================

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('Copied to clipboard!', 'success');
    }).catch(() => {
        showNotification('Failed to copy', 'error');
    });
}

// ===================================
// Export Results
// ===================================

function exportResults(result) {
    const data = {
        prediction: result.prediction,
        confidence: result.confidence,
        message: result.message,
        timestamp: result.timestamp,
        model: result.model_name
    };
    
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `spam-detection-${Date.now()}.json`;
    a.click();
    URL.revokeObjectURL(url);
    
    showNotification('Results exported!', 'success');
}

// ===================================
// Loading State Management
// ===================================

function setLoadingState(button, isLoading) {
    if (isLoading) {
        button.disabled = true;
        button.dataset.originalText = button.innerHTML;
        button.innerHTML = '<span class="loading-spinner" style="width: 20px; height: 20px; border-width: 2px;"></span> Processing...';
    } else {
        button.disabled = false;
        button.innerHTML = button.dataset.originalText;
    }
}

// ===================================
// Mobile Menu Toggle
// ===================================

function initMobileMenu() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;
    
    // Create mobile menu button
    const menuButton = document.createElement('button');
    menuButton.className = 'mobile-menu-toggle';
    menuButton.innerHTML = '☰';
    menuButton.style.cssText = `
        display: none;
        background: none;
        border: none;
        font-size: 1.5rem;
        cursor: pointer;
        color: var(--text-color);
    `;
    
    // Add to navbar
    const navBrand = navbar.querySelector('.nav-brand');
    navBrand.parentElement.insertBefore(menuButton, navBrand.nextSibling);
    
    // Toggle menu on click
    menuButton.addEventListener('click', () => {
        const navMenu = navbar.querySelector('.nav-menu');
        navMenu.classList.toggle('active');
    });
    
    // Show button on mobile
    const mediaQuery = window.matchMedia('(max-width: 768px)');
    function handleMobile(e) {
        if (e.matches) {
            menuButton.style.display = 'block';
        } else {
            menuButton.style.display = 'none';
        }
    }
    mediaQuery.addListener(handleMobile);
    handleMobile(mediaQuery);
}

// ===================================
// Statistics Counter Animation
// ===================================

function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    
    counters.forEach(counter => {
        const target = counter.textContent;
        const isPercentage = target.includes('%');
        const numericValue = parseInt(target.replace(/\D/g, ''));
        
        if (isNaN(numericValue)) return;
        
        let current = 0;
        const increment = numericValue / 50;
        const timer = setInterval(() => {
            current += increment;
            if (current >= numericValue) {
                counter.textContent = target;
                clearInterval(timer);
            } else {
                counter.textContent = Math.floor(current) + (isPercentage ? '%' : '+');
            }
        }, 30);
    });
}

// ===================================
// Initialize on Page Load
// ===================================

document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initSmoothScroll();
    initScrollAnimations();
    initCharacterCounter();
    initKeyboardShortcuts();
    initMobileMenu();
    
    // Animate counters when they come into view
    const statsSection = document.querySelector('.stats');
    if (statsSection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounters();
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        
        observer.observe(statsSection);
    }
    
    // Add keyboard shortcut hints
    const detectPage = document.querySelector('.detection-section');
    if (detectPage) {
        console.log('Keyboard Shortcuts:');
        console.log('Ctrl/Cmd + Enter: Check for spam');
        console.log('Ctrl/Cmd + K: Clear input');
        console.log('Ctrl/Cmd + L: Load sample');
    }
});

// ===================================
// Service Worker Registration (PWA)
// ===================================

if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        // Uncomment to enable PWA features
        // navigator.serviceWorker.register('/sw.js')
        //     .then(reg => console.log('Service Worker registered'))
        //     .catch(err => console.log('Service Worker registration failed'));
    });
}

// ===================================
// Error Handling
// ===================================

window.addEventListener('error', (e) => {
    console.error('Global error:', e.error);
    // Don't show notification for every error, only critical ones
});

window.addEventListener('unhandledrejection', (e) => {
    console.error('Unhandled promise rejection:', e.reason);
});

// ===================================
// Utility Functions
// ===================================

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Export functions for use in HTML
window.toggleTheme = toggleTheme;
window.showNotification = showNotification;
window.copyToClipboard = copyToClipboard;
window.exportResults = exportResults;
