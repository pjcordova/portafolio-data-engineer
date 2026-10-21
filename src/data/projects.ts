// Datos estáticos de los proyectos mostrados en "Casos de Éxito".
// Edita este archivo para actualizar el portafolio (no requiere base de datos).
// Las maquetas (campo `mockup`) son recreaciones genéricas en HTML/CSS/Bootstrap,
// no capturas ni accesos reales a los sistemas de los clientes.

export interface Project {
  slug: string;
  nombre: string;
  cliente?: string;
  categoria: string;
  problemaResuelto: string;
  proceso: string[];
  tecnologias: string[];
  status: 'Completado' | 'En Progreso';
  ilustracion: string;
  mockup: string;
  /** Alto del iframe de la maqueta (clases Tailwind). Por defecto 'h-80'. */
  mockupAlto?: string;
  /** Resultados medidos (opcional): 2-4 frases cortas con números concretos. */
  resultados?: string[];
  /**
   * URL pública del sitio en vivo (opcional). Úsalo solo cuando el sitio es
   * de acceso público y no expone datos/paneles internos del cliente (p. ej.
   * una tienda online), no para sistemas internos tipo ERP.
   */
  linkSitio?: string;
}

export const projects: Project[] = [
  {
    slug: 'extractos-verdes-chavely',
    nombre: 'Chavely ERP',
    cliente: 'Extractos Verdes Chavely',
    categoria: 'ERP Móvil · Caja, Inventario y Reportes',
    problemaResuelto:
      'La venta se registraba en varios medios de pago (efectivo, Yape, Plin, transferencias) sin un control centralizado, lo que dificultaba cuadrar caja, medir gastos por categoría y saber qué quedaba en stock.',
    proceso: [
      'Descubrimiento: mapeo del flujo diario de caja, egresos directos e ingreso de mercadería del negocio.',
      'Diseño: priorizado para uso 100% desde celular, pensado para registrar una venta en segundos.',
      'Desarrollo: módulo de registro rápido (multi-medio de pago), panel gerencial con reportes y auditoría, e inventario por proveedor.',
      'Entrega: despliegue, capacitación del equipo y ajustes según el uso real día a día.',
    ],
    tecnologias: ['Vue 3', 'TypeScript', 'Supabase', 'PostgreSQL', 'Tailwind CSS'],
    status: 'Completado',
    ilustracion: '/proyectos/erp-financiero.svg',
    mockup: '/proyectos/mockups/erp-chavely.html',
    mockupAlto: 'h-[640px]',
  },
  {
    slug: 'bithia-web',
    nombre: 'Bithia Web',
    cliente: 'Bithia Brand',
    categoria: 'E-commerce de Moda',
    problemaResuelto:
      'El inventario real de Bithia vivía en su ERP y las ventas ocurrían por WhatsApp, sin ningún puente entre ambos: cada consulta de stock se revisaba a mano y, si se concretaba la venta, también se descontaba a mano. A eso se suma que el stand renueva mercadería cada 15 días con unidades limitadas, así que quien no pasaba esa semana no se enteraba de lo nuevo.',
    proceso: [
      'Descubrimiento: identificar que el problema no era la falta de catálogo, sino la falta de puente entre el ERP (dueño del inventario) y WhatsApp (donde ocurría la venta).',
      'Diseño: catálogo autogestionable por la dueña (sin pedir despliegues a nadie), pago por Yape/Plin con comprobante adjunto y sin pasarela de pago.',
      'Desarrollo: cada bug se reprodujo con datos reales antes de tocar código (p. ej. un scroll horizontal fantasma en móvil rastreado hasta un carrusel que inflaba el ancho del documento), y cada mejora se midió antes/después — incluido un endpoint de stock que llegó a generar ~12 consultas/segundo al ERP y se reescribió con límite por IP y caché.',
      'Entrega: despliegue en Vercel con verificación en producción (rutas, consola, red) y la integración con el ERP lista, pendiente solo de activar credenciales.',
    ],
    tecnologias: ['Next.js 15', 'React 19', 'TypeScript', 'Tailwind CSS', 'Prisma + PostgreSQL (Neon)', 'Cloudinary', 'Vercel'],
    status: 'Completado',
    ilustracion: '/proyectos/ecommerce.svg',
    mockup: '/proyectos/mockups/bithia-web.html',
    mockupAlto: 'h-[560px]',
    resultados: [
      'De ~12 a 0 consultas/segundo al ERP al navegar portada y catálogo; una compra completa cuesta 3.',
      'Endpoint de stock protegido: 70 peticiones en ráfaga → solo 2 llegaron al ERP.',
      '~8,000 líneas de TypeScript en 64 archivos · 6 tablas en PostgreSQL · 17 prendas publicadas.',
    ],
    linkSitio: 'https://bithia-web.vercel.app/',
  },
  {
    slug: 'aibplus',
    nombre: 'AIB+',
    categoria: 'Marketplace B2B de Tecnología',
    problemaResuelto:
      'Un negocio que quiere una web, CRM, ERP, automatización o app no sabe por dónde empezar ni cuánto le costará, y encontrar un ingeniero de confianza toma tiempo. AIB+ deja ver gratis cómo quedaría el proyecto (con su nombre y colores) y comparar propuestas de ingenieros verificados antes de pagar nada.',
    proceso: [
      'Descubrimiento: mapeo de los servicios más pedidos por pequeños negocios (web, CRM, ERP, automatización, apps).',
      'Diseño: flujo de "mira cómo quedaría antes de pagar", sin necesidad de crear cuenta.',
      'Desarrollo: catálogo de diseños por rubro, perfiles de ingenieros verificados y seguimiento de propuestas.',
      'Entrega: lanzamiento como producto de Cordova Solutions y mejora continua según el uso real.',
    ],
    tecnologias: ['Vue 3', 'TypeScript', 'Supabase', 'Tailwind CSS'],
    status: 'En Progreso',
    ilustracion: '/proyectos/edtech-ia.svg',
    mockup: '/proyectos/mockups/aibplus.html',
    mockupAlto: 'h-[520px]',
  },
];
