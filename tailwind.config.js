/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./*/templates/*.html'],
  theme: {
    extend: {},
    fontFamily: {
      'berkeley': ['Berkeley Mono', 'monospace'],
      'ibm-plex': ['IBM Plex Mono', 'monospace']
    }
  },
  plugins: [],
}
