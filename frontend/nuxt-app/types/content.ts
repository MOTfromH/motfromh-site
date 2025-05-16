export interface Content {
  id: number
  title: string
  description: string | null
  body?: string | null
  image_url?: string | null
  gallery?: string[] | null
  links?: Record<string, string> | null
  has_view: boolean
  created_at: string   // ISO-Datum
}