document.addEventListener('DOMContentLoaded', () => {

    const toast = document.getElementById('toast');
    let toastTimeout;

    function showToast(message) {
        if(!toast) return;
        toast.textContent = message;
        toast.classList.add('show');
        if (toastTimeout) clearTimeout(toastTimeout);
        toastTimeout = setTimeout(() => {
            toast.classList.remove('show');
        }, 3000);
    }

    // Modal / Window Logic
    const openBtns = document.querySelectorAll('.open-window');
    const closeBtns = document.querySelectorAll('.win-close');
    const overlay = document.getElementById('windowOverlay');
    const windows = document.querySelectorAll('.rabbit-hole');

    function closeAllWindows() {
        windows.forEach(win => win.classList.remove('active'));
        if(overlay) overlay.classList.remove('active');
    }

    openBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-target');
            const targetWindow = document.getElementById(targetId);
            
            // Close others first
            closeAllWindows();
            
            // Open target
            if (targetWindow) {
                targetWindow.classList.add('active');
                if(overlay) overlay.classList.add('active');
            }
        });
    });

    closeBtns.forEach(btn => {
        btn.addEventListener('click', closeAllWindows);
    });

    // Close on overlay click
    if (overlay) {
        overlay.addEventListener('click', closeAllWindows);
    }

    // Copy Button Logic
    const copyBtns = document.querySelectorAll('.copy-btn');
    copyBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-target');
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const textToCopy = targetElement.innerText || targetElement.textContent;
                navigator.clipboard.writeText(textToCopy.trim()).then(() => {
                    showToast('TEXT COPIED TO CLIPBOARD');
                    const originalText = btn.textContent;
                    btn.textContent = 'COPIED!';
                    setTimeout(() => {
                        btn.textContent = originalText;
                    }, 2000);
                }).catch(err => {
                    console.error('Failed to copy text: ', err);
                });
            }
        });
    });
    
    // Small Link Copy Logic
    const smallCopyBtns = document.querySelectorAll('.small-copy');
    smallCopyBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const textToCopy = btn.getAttribute('data-copy');
            if(textToCopy) {
                navigator.clipboard.writeText(textToCopy.trim()).then(() => {
                    showToast('LINK COPIED');
                    const originalText = btn.textContent;
                    btn.textContent = 'COPIED';
                    setTimeout(() => {
                        btn.textContent = originalText;
                    }, 1500);
                }).catch(err => {
                    console.error('Failed to copy link: ', err);
                });
            }
        });
    });

});
