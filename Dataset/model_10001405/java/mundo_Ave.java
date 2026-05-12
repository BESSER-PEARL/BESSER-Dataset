





import java.util.List;
import java.util.ArrayList;

public class mundo_Ave  {

    private String factorPeso;
    private String altura;
    private String color;



    public mundo_Ave(
        String factorPeso,        String altura,        String color    ) {
        this.factorPeso = factorPeso;
        this.altura = altura;
        this.color = color;
    }


    public String getFactorpeso() {
        return factorPeso;
    }

    public void setFactorpeso(String factorPeso) {
        this.factorPeso = factorPeso;
    }
    public String getAltura() {
        return altura;
    }

    public void setAltura(String altura) {
        this.altura = altura;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}