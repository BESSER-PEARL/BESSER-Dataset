





import java.util.List;
import java.util.ArrayList;

public class caracteristica_Caracteristica extends Elemento {






    private caracteristica_Caracteristica caracteristica_caracteristica;




    private caracteristica_Atributo caracteristica_atributo;




    private List<caracteristica_Atributo> caracteristica_atributos;




    private List<caracteristica_ElementoExterno> caracteristica_elementoexternos;




    private caracteristica_Caracteristica caracteristica_caracteristica;


    public caracteristica_Caracteristica(
    ) {
        super(
        );
        this.caracteristica_atributos = new ArrayList<>();
        this.caracteristica_elementoexternos = new ArrayList<>();
    }

    public caracteristica_Caracteristica(
        ArrayList<caracteristica_Atributo> caracteristica_atributos,        ArrayList<caracteristica_ElementoExterno> caracteristica_elementoexternos    ) {
        this.caracteristica_atributos = caracteristica_atributos;
        this.caracteristica_elementoexternos = caracteristica_elementoexternos;
    }


    public caracteristica_Caracteristica getCaracteristica_caracteristica() {
        return caracteristica_caracteristica;
    }

    public void setCaracteristica_caracteristica(caracteristica_Caracteristica caracteristica_caracteristica) {
        this.caracteristica_caracteristica = caracteristica_caracteristica;
    }
    public caracteristica_Atributo getCaracteristica_atributo() {
        return caracteristica_atributo;
    }

    public void setCaracteristica_atributo(caracteristica_Atributo caracteristica_atributo) {
        this.caracteristica_atributo = caracteristica_atributo;
    }
    public List<caracteristica_Atributo> getCaracteristica_atributos() {
        return caracteristica_atributos;
    }

    public void addCaracteristica_atributo(Caracteristica_atributo caracteristica_atributo) {
        this.caracteristica_atributos.add(caracteristica_atributo);
    }
    public List<caracteristica_ElementoExterno> getCaracteristica_elementoexternos() {
        return caracteristica_elementoexternos;
    }

    public void addCaracteristica_elementoexterno(Caracteristica_elementoexterno caracteristica_elementoexterno) {
        this.caracteristica_elementoexternos.add(caracteristica_elementoexterno);
    }
    public caracteristica_Caracteristica getCaracteristica_caracteristica() {
        return caracteristica_caracteristica;
    }

    public void setCaracteristica_caracteristica(caracteristica_Caracteristica caracteristica_caracteristica) {
        this.caracteristica_caracteristica = caracteristica_caracteristica;
    }

}