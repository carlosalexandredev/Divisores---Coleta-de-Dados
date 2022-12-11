
public class Divisores {

  public static void main(String[] args) {
		long numero, i, cont=0;
		numero = Long.parseLong(args[0]);
		System.out.println("Calculando a quantidade de divisores para "+numero);
		if (numero<=0) System.exit(0);
		
		long inicio, fim;
		inicio = System.currentTimeMillis();
		for (i=1;i<=numero;++i) {
			if (numero%i==0) ++cont;
		}
		fim = System.currentTimeMillis();
		double secs = (fim-inicio)/1000.0;
		System.out.println("tempo gasto "+secs);
		System.out.println("O numero de divisores e "+cont);
  }
  
}
