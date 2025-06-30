// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },

  modules: [
    '@nuxt/ui',
    '@nuxt/eslint',
    '@nuxt/image',
  ],

  plugins: [
    '~/plugins/bootstrap.client.ts'
  ],

  css: [
    'bootstrap/dist/css/bootstrap.min.css',
    '~/assets/css/main.css'
  ],

  // runtimeConfig: {
  //   serverSide: {
  //     apiBase: process.env.NUXT_SERVERAPI_BASE || 'http://api:8000/api/v1'
  //   },
  //   public: {
  //     apiBase: process.env.NUXT_PUBLICAPI_BASE || 'http://localhost:8800/api/v1'
  //   }
  // },

  image: {
    dirs: ['public'],
    provider: 'ipx',
    presets: {
      default: {
        modifiers: {
          format: 'webp',
          quality: 75,
        },
      },
    },
    domains: [],
  },
})
