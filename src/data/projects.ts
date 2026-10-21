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
      'Bithia vendía solo desde su stand físico en Polvos Azules (Ica), sin forma de mostrar su catálogo ni recibir pedidos fuera de ese horario y lugar. Necesitaban una tienda online simple, sin pasarela de pago compleja, que derive el pedido a WhatsApp para coordinar entrega y pago.',
    proceso: [
      'Descubrimiento: entender el flujo real de venta en el stand (catálogo rotativo cada 15 días, pocas unidades por modelo).',
      'Diseño: identidad cálida y editorial (tonos tierra), pensada para mostrar prendas como protagonistas.',
      'Desarrollo: catálogo filtrable por categoría y talla, ficha de producto y carrito que termina la compra por WhatsApp.',
      'Entrega: despliegue en Vercel y ajustes de catálogo según la rotación real de mercadería.',
    ],
    tecnologias: ['Vue 3', 'TypeScript', 'Supabase', 'Tailwind CSS', 'Vercel'],
    status: 'Completado',
    ilustracion: '/proyectos/ecommerce.svg',
    mockup: '/proyectos/mockups/bithia-web.html',
    mockupAlto: 'h-[560px]',
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
