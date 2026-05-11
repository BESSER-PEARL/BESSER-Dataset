





import java.util.List;
import java.util.ArrayList;

public class caracteristica_VariacaoDoisProduto extends CaracteristicaProduto, ElementoDeProduto {

    private String cardinalidadeMaxima;



    public caracteristica_VariacaoDoisProduto(
        String cardinalidadeMaxima    ) {
        super(
        );
        this.cardinalidadeMaxima = cardinalidadeMaxima;
    }


    public String getCardinalidademaxima() {
        return cardinalidadeMaxima;
    }

    public void setCardinalidademaxima(String cardinalidadeMaxima) {
        this.cardinalidadeMaxima = cardinalidadeMaxima;
    }


}