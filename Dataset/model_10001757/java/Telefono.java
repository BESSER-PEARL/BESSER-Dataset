





import java.util.List;
import java.util.ArrayList;

public class Telefono  {

    private int Prefijo;
    private int Codigo_de_Area;
    private int Numero;



    public Telefono(
        int Prefijo,        int Codigo_de_Area,        int Numero    ) {
        this.Prefijo = Prefijo;
        this.Codigo_de_Area = Codigo_de_Area;
        this.Numero = Numero;
    }


    public int getPrefijo() {
        return Prefijo;
    }

    public void setPrefijo(int Prefijo) {
        this.Prefijo = Prefijo;
    }
    public int getCodigo_de_area() {
        return Codigo_de_Area;
    }

    public void setCodigo_de_area(int Codigo_de_Area) {
        this.Codigo_de_Area = Codigo_de_Area;
    }
    public int getNumero() {
        return Numero;
    }

    public void setNumero(int Numero) {
        this.Numero = Numero;
    }


}