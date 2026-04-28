import { createClient } from '@supabase/supabase-js'

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL || 'https://dcamnifuwopamavlxwhh.supabase.co'
// Nota: Deberás agregar tu ANON_KEY en el archivo .env como VITE_SUPABASE_ANON_KEY
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY || ''

export const supabase = createClient(supabaseUrl, supabaseAnonKey)
