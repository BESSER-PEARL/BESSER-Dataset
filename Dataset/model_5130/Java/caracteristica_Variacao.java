





import java.util.List;
import java.util.ArrayList;

public class caracteristica_Variacao extends Elemento, PontoDeVariacao {

    private String cardinalidadeMaxima;
    private String cardinalidadeMinima;





    private caracteristica_Caracteristica caracteristica_caracteristica;




    private caracteristica_Caracteristica caracteristica_caracteristica;


    public caracteristica_Variacao(
        String cardinalidadeMaxima,        String cardinalidadeMinima    ) {
        super(
        );
        this.cardinalidadeMaxima = cardinalidadeMaxima;
        this.cardinalidadeMinima = cardinalidadeMinima;
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
    public caracteristica_Caracteristica getCaracteristica_caracteristica() {
        return caracteristica_caracteristica;
    }

    public void setCaracteristica_caracteristica(caracteristica_Caracteristica caracteristica_caracteristica) {
        this.caracteristica_caracteristica = caracteristica_caracteristica;
    }

}