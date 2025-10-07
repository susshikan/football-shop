;(function () {
  function ensureContainer() {
    let container = document.getElementById('toast-container')
    if (!container) {
      container = document.createElement('div')
      container.id = 'toast-container'
      container.className = [
        'fixed',
        'bottom-6',
        'right-6',
        'z-50',
        'flex',
        'flex-col',
        'gap-3',
        'pointer-events-none',
      ].join(' ')
      document.body.appendChild(container)
    }
    return container
  }

  function buildToast(title, message, type) {
    const wrapper = document.createElement('div')
    wrapper.className = 'pointer-events-auto'

    const base = [
      'w-80',
      'max-w-[90vw]',
      'bg-white',
      'border',
      'rounded-xl',
      'shadow-soft',
      'p-4',
      'flex',
      'items-start',
      'gap-3',
      'transition',
      'duration-300',
      'ease-out',
      'transform',
      'translate-y-4',
      'opacity-0',
    ]

    let borderClass = 'border-neutral-200/80'
    let iconBg = 'bg-ink/10'
    let iconText = 'text-ink'
    if (type === 'success') {
      borderClass = 'border-gold'
      iconBg = 'bg-gold/15'
      iconText = 'text-gold'
    } else if (type === 'error') {
      borderClass = 'border-burgundy'
      iconBg = 'bg-burgundy/15'
      iconText = 'text-burgundy'
    } else if (type === 'info' || type === 'normal' || !type) {
      borderClass = 'border-neutral-200/80'
      iconBg = 'bg-ink/10'
      iconText = 'text-ink'
    }

    const card = document.createElement('div')
    card.className = [...base, borderClass].join(' ')

    const icon = document.createElement('div')
    icon.className = ['mt-0.5', 'h-6', 'w-6', 'rounded-full', iconBg, 'flex', 'items-center', 'justify-center', iconText, 'shrink-0'].join(' ')
    icon.innerHTML = type === 'error'
      ? '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-3.5 w-3.5"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm-1-5a1 1 0 112 0 1 1 0 01-2 0zm1-8a1 1 0 00-1 1v5a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/></svg>'
      : '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-3.5 w-3.5"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.707a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 10-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>'

    const content = document.createElement('div')
    content.className = 'flex-1 min-w-0'

    const ttl = document.createElement('div')
    ttl.className = 'text-sm font-semibold text-ink truncate'
    ttl.textContent = title || ''

    const msg = document.createElement('div')
    msg.className = 'mt-0.5 text-sm text-neutral-600'
    msg.textContent = message || ''

    // Close button
    const closeBtn = document.createElement('button')
    closeBtn.className = 'ml-1 p-1 text-neutral-400 hover:text-ink rounded transition'
    closeBtn.setAttribute('aria-label', 'Close')
    closeBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-4 w-4"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>'

    content.appendChild(ttl)
    content.appendChild(msg)
    card.appendChild(icon)
    card.appendChild(content)
    card.appendChild(closeBtn)
    wrapper.appendChild(card)

    closeBtn.addEventListener('click', () => dismiss(wrapper))
    wrapper.addEventListener('mouseenter', () => wrapper.dataset.paused = '1')
    wrapper.addEventListener('mouseleave', () => delete wrapper.dataset.paused)

    // Enter animation (next frame to allow transition)
    requestAnimationFrame(() => {
      card.classList.remove('translate-y-4', 'opacity-0')
      card.classList.add('translate-y-0', 'opacity-100')
    })

    return wrapper
  }

  function dismiss(wrapper) {
    const card = wrapper.firstElementChild
    if (!card) return
    card.classList.remove('translate-y-0', 'opacity-100')
    card.classList.add('translate-y-4', 'opacity-0')
    setTimeout(() => wrapper.remove(), 250)
  }

  window.showToast = function (title, message, type = 'info', duration = 3000) {
    const container = ensureContainer()
    const toast = buildToast(title, message, type)
    container.appendChild(toast)

    // Auto dismiss with pause-on-hover
    const start = Date.now()
    let remaining = duration
    let timer = setTimeout(() => dismiss(toast), remaining)

    const onHoverChange = () => {
      if (toast.dataset.paused) {
        clearTimeout(timer)
        remaining -= Date.now() - start
      } else {
        timer = setTimeout(() => dismiss(toast), Math.max(0, remaining))
      }
    }
    toast.addEventListener('mouseenter', onHoverChange)
    toast.addEventListener('mouseleave', onHoverChange)
  }
})()
