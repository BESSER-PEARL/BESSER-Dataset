





import java.util.List;
import java.util.ArrayList;

public class caracteristica_VariacaoDois extends ElementoCaracteristico, Caracteristica {

    private String cardinalidadeMaxima;
    private String cardinalidadeMaximaOr;
    private String cardinalidadeMinimaOr;



    public caracteristica_VariacaoDois(
        String cardinalidadeMaxima,        String cardinalidadeMaximaOr,        String cardinalidadeMinimaOr    ) {
        super(
        );
        this.cardinalidadeMaxima = cardinalidadeMaxima;
        this.cardinalidadeMaximaOr = cardinalidadeMaximaOr;
        this.cardinalidadeMinimaOr = cardinalidadeMinimaOr;
    }


    public String getCardinalidademaxima() {
        return cardinalidadeMaxima;
    }

    public void setCardinalidademaxima(String cardinalidadeMaxima) {
        this.cardinalidadeMaxima = cardinalidadeMaxima;
    }
    public String getCardinalidademaximaor() {
        return cardinalidadeMaximaOr;
    }

    public void setCardinalidademaximaor(String cardinalidadeMaximaOr) {
        this.cardinalidadeMaximaOr = cardinalidadeMaximaOr;
    }
    public String getCardinalidademinimaor() {
        return cardinalidadeMinimaOr;
    }

    public void setCardinalidademinimaor(String cardinalidadeMinimaOr) {
        this.cardinalidadeMinimaOr = cardinalidadeMinimaOr;
    }


}