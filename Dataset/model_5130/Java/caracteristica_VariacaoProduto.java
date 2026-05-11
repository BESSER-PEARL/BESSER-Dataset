





import java.util.List;
import java.util.ArrayList;

public class caracteristica_VariacaoProduto extends ElementoDeProduto {

    private String cardinalidadeMaxima;
    private String cardinalidadeMinima;





    private caracteristica_CaracteristicaProduto caracteristica_caracteristicaproduto;


    public caracteristica_VariacaoProduto(
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

    public caracteristica_CaracteristicaProduto getCaracteristica_caracteristicaproduto() {
        return caracteristica_caracteristicaproduto;
    }

    public void setCaracteristica_caracteristicaproduto(caracteristica_CaracteristicaProduto caracteristica_caracteristicaproduto) {
        this.caracteristica_caracteristicaproduto = caracteristica_caracteristicaproduto;
    }

}