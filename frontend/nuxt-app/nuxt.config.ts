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
    'bootstrap/dist/css/bootstrap.min.css'
  ],

  // https://image.nuxt.com/get-started/configuration
  image: {
    dirs: ['assets/images'],
    // optional: provider
    provider: 'ipx',
    // optional: IPX configuration
    presets: {
      default: {
        modifiers: {
          format: 'webp',
          quality: 75,
        },
      },
    },
    // optional: allow domains 
    domains: [],
  },
})