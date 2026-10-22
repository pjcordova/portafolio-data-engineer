// Testimonios reales de clientes. La sección no se muestra en el sitio
// mientras este arreglo esté vacío (ver TestimoniosSection.vue).
//
// Para agregar uno, copia este formato con una frase REAL de un cliente
// (Chavely ERP, Bithia Web, AIB+, Buen Vivir, etc.) — nunca inventada:
//
// {
//   cita: 'La frase textual del cliente, tal como la dijo o escribió.',
//   autor: 'Nombre de la persona',
//   cargo: 'Su cargo o relación con el proyecto',
//   empresa: 'Nombre de la empresa',
//   puntuacion: 5, // 1 a 5
// }

export interface Testimonio {
  cita: string;
  autor: string;
  cargo: string;
  empresa: string;
  puntuacion: number;
}

export const testimonios: Testimonio[] = [];
