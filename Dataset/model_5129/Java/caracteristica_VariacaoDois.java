





import java.util.List;
import java.util.ArrayList;

public class caracteristica_VariacaoDois extends ElementoCaracteristico, Caracteristica {

    private String cardinalidadeMinimaOr;
    private String cardinalidadeMaximaOr;
    private String cardinalidadeMaxima;



    public caracteristica_VariacaoDois(
        String cardinalidadeMinimaOr,        String cardinalidadeMaximaOr,        String cardinalidadeMaxima    ) {
        super(
        );
        this.cardinalidadeMinimaOr = cardinalidadeMinimaOr;
        this.cardinalidadeMaximaOr = cardinalidadeMaximaOr;
        this.cardinalidadeMaxima = cardinalidadeMaxima;
    }


    public String getCardinalidademinimaor() {
        return cardinalidadeMinimaOr;
    }

    public void setCardinalidademinimaor(String cardinalidadeMinimaOr) {
        this.cardinalidadeMinimaOr = cardinalidadeMinimaOr;
    }
    public String getCardinalidademaximaor() {
        return cardinalidadeMaximaOr;
    }

    public void setCardinalidademaximaor(String cardinalidadeMaximaOr) {
        this.cardinalidadeMaximaOr = cardinalidadeMaximaOr;
    }
    public String getCardinalidademaxima() {
        return cardinalidadeMaxima;
    }

    public void setCardinalidademaxima(String cardinalidadeMaxima) {
        this.cardinalidadeMaxima = cardinalidadeMaxima;
    }


}