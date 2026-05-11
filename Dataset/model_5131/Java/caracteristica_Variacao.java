





import java.util.List;
import java.util.ArrayList;

public class caracteristica_Variacao extends Elemento, PontoDeVariacao {

    private String cardinalidadeMaxima;
    private String cardinalidadeMinima;





    private caracteristica_Caracteristica caracteristica_caracteristica;




    private List<caracteristica_Variante> caracteristica_variantes;




    private caracteristica_Variante caracteristica_variante;




    private caracteristica_Caracteristica caracteristica_caracteristica;


    public caracteristica_Variacao(
        String cardinalidadeMaxima,        String cardinalidadeMinima    ) {
        super(
        );
        this.cardinalidadeMaxima = cardinalidadeMaxima;
        this.cardinalidadeMinima = cardinalidadeMinima;
        this.caracteristica_variantes = new ArrayList<>();
    }

    public caracteristica_Variacao(
        String cardinalidadeMaxima,        String cardinalidadeMinima        ArrayList<caracteristica_Variante> caracteristica_variantes    ) {
        this.cardinalidadeMaxima = cardinalidadeMaxima;
        this.cardinalidadeMinima = cardinalidadeMinima;
        this.caracteristica_variantes = caracteristica_variantes;
    }

    public String getCardinalidademaxima() {
        return cardinalidadeMaxima;
    }

    public void setCardinalidademaxima(String cardinalidadeMaxima) {
        this.cardinalidadeMaxima = cardinalidadeMaxima;
    }
    public String getCardinalidademinima() {
        return cardinalidadeMinima;
    }

    public void setCardinalidademinima(String cardinalidadeMinima) {
        this.cardinalidadeMinima = cardinalidadeMinima;
    }

    public caracteristica_Caracteristica getCaracteristica_caracteristica() {
        return caracteristica_caracteristica;
    }

    public void setCaracteristica_caracteristica(caracteristica_Caracteristica caracteristica_caracteristica) {
        this.caracteristica_caracteristica = caracteristica_caracteristica;
    }
    public List<caracteristica_Variante> getCaracteristica_variantes() {
        return caracteristica_variantes;
    }

    public void addCaracteristica_variante(Caracteristica_variante caracteristica_variante) {
        this.caracteristica_variantes.add(caracteristica_variante);
    }
    public caracteristica_Variante getCaracteristica_variante() {
        return caracteristica_variante;
    }

    public void setCaracteristica_variante(caracteristica_Variante caracteristica_variante) {
        this.caracteristica_variante = caracteristica_variante;
    }
    public caracteristica_Caracteristica getCaracteristica_caracteristica() {
        return caracteristica_caracteristica;
    }

    public void setCaracteristica_caracteristica(caracteristica_Caracteristica caracteristica_caracteristica) {
        this.caracteristica_caracteristica = caracteristica_caracteristica;
    }

}