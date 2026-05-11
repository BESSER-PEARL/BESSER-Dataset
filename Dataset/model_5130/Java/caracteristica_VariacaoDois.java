





import java.util.List;
import java.util.ArrayList;

public class caracteristica_VariacaoDois extends Caracteristica, ElementoCaracteristico {

    private String cardinalidadeMaxima;
    private String cardinalidadeMinimaOr;
    private String cardinalidadeMaximaOr;



    public caracteristica_VariacaoDois(
        String cardinalidadeMaxima,        String cardinalidadeMinimaOr,        String cardinalidadeMaximaOr    ) {
        super(
        );
        this.cardinalidadeMaxima = cardinalidadeMaxima;
        this.cardinalidadeMinimaOr = cardinalidadeMinimaOr;
        this.cardinalidadeMaximaOr = cardinalidadeMaximaOr;
    }


    public String getCardinalidademaxima() {
        return cardinalidadeMaxima;
    }

    public void setCardinalidademaxima(String cardinalidadeMaxima) {
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


}