import type { Content } from '@/types/content'

export const useContent = () => {
  const getApiUrl = (endpoint: string) => {
    if (import.meta.server) {
      // SSR: interner Docker-Hostname
      const host = process.env.BACKEND_HOST || 'api'
      return `http://${host}:8000/api/v1${endpoint}`
    }
    // Client: relative Aufrufe, gehen über deinen Proxy
    return `/api/v1${endpoint}`
  }

  const fetchContent = async () => {
    const url = getApiUrl('/content/')
    return await $fetch<Content[]>(url)
  }

  return { fetchContent }
}
