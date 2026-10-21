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
      'El dueño de un negocio quiere una web, un CRM o una app, pero no sabe explicar lo que necesita ni cuánto debería costar, y cotizar le resulta confuso y arriesgado. Del otro lado, el ingeniero pierde horas cotizando a clientes que no saben lo que quieren, y consigue clientes solo de boca en boca o en plataformas que le cobran comisión. AIB+ conecta a ambos: el cliente ve gratis, en un minuto, cómo quedaría su proyecto antes de pagar nada, y el ingeniero lo recibe con todo claro — sin comisión, solo con una membresía.',
    proceso: [
      'Descubrimiento: el cuello de botella no era la tecnología sino la cotización — clientes que no saben pedir, ingenieros que pierden horas cotizando en frío.',
      'Diseño: flujo sin fricción para el cliente (cuestionario corto, maqueta editable con su nombre y colores, sin crear cuenta) y un panel para el ingeniero con documentación técnica generada por IA.',
      'Desarrollo: ABI, el asistente del ingeniero (con Claude Opus), agenda reuniones por Google Meet, redacta mensajes y arma propuestas; el avance se paga y aprueba por etapas, con 0% de comisión para el ingeniero.',
      'Entrega: ciclos cortos de construir, publicar y medir — cada cambio se despliega solo en Vercel, y las decisiones se validan con datos reales de dónde llegan los clientes, cuántos prueban y cuántos aceptan.',
    ],
    tecnologias: ['React 19', 'TypeScript', 'Vite 7', 'Tailwind CSS 4', 'Node.js + Express 5', 'Supabase (PostgreSQL)', 'Claude (Sonnet + Opus 5.5)', 'Vercel'],
    status: 'En Progreso',
    ilustracion: '/proyectos/edtech-ia.svg',
    mockup: '/proyectos/mockups/aibplus.html',
    mockupAlto: 'h-[520px]',
  },
];
