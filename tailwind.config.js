/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  future: {
    // hover:/group-hover: only apply on devices that actually support hover
    // (prevents hover states sticking on tap on touch screens).
    hoverOnlyWhenSupported: true,
  },
  theme: {
    extend: {
      colors: {
        ink: '#131210',
        paper: '#FAF8F4',
        accent: {
          50: '#EEF2FF',
          100: '#DCE4FF',
          300: '#94A9FF',
          500: '#2F5BFF',
          600: '#1F43E6',
          700: '#1733B3',
        },
        gold: {
          DEFAULT: '#C9A24A',
          light: '#E3C27E',
          dark: '#8B6B2E',
        },
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        serif: ['"Instrument Serif"', 'Georgia', 'serif'],
      },
      transitionTimingFunction: {
        'out-expo': 'cubic-bezier(0.16, 1, 0.3, 1)',
      },
      keyframes: {
        'fade-up': {
          '0%': { opacity: '0', transform: 'translateY(14px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
      },
      animation: {
        'fade-up': 'fade-up 0.7s cubic-bezier(0.16, 1, 0.3, 1) both',
      },
    },
  },
  plugins: [],
}
