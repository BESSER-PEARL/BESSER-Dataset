





import java.util.List;
import java.util.ArrayList;

public class caracteristica_CaracteristicaProduto extends ElementoDeProduto {






    private caracteristica_CaracteristicaProduto caracteristica_caracteristicaproduto;




    private List<caracteristica_CaracteristicaProduto> caracteristica_caracteristicaprodutos;


    public caracteristica_CaracteristicaProduto(
    ) {
        super(
        );
        this.caracteristica_caracteristicaprodutos = new ArrayList<>();
    }

    public caracteristica_CaracteristicaProduto(
        ArrayList<caracteristica_CaracteristicaProduto> caracteristica_caracteristicaprodutos    ) {
        this.caracteristica_caracteristicaprodutos = caracteristica_caracteristicaprodutos;
    }


    public caracteristica_CaracteristicaProduto getCaracteristica_caracteristicaproduto() {
        return caracteristica_caracteristicaproduto;
    }

    public void setCaracteristica_caracteristicaproduto(caracteristica_CaracteristicaProduto caracteristica_caracteristicaproduto) {
        this.caracteristica_caracteristicaproduto = caracteristica_caracteristicaproduto;
    }
    public List<caracteristica_CaracteristicaProduto> getCaracteristica_caracteristicaprodutos() {
        return caracteristica_caracteristicaprodutos;
    }

    public void addCaracteristica_caracteristicaproduto(Caracteristica_caracteristicaproduto caracteristica_caracteristicaproduto) {
        this.caracteristica_caracteristicaprodutos.add(caracteristica_caracteristicaproduto);
    }

}