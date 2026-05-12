





import java.util.List;
import java.util.ArrayList;

public class venta  {

    private String Setcodigo;
    private String setFecha;



    public venta(
        String Setcodigo,        String setFecha    ) {
        this.Setcodigo = Setcodigo;
        this.setFecha = setFecha;
    }


    public String getSetcodigo() {
        return Setcodigo;
    }

    public void setSetcodigo(String Setcodigo) {
        this.Setcodigo = Setcodigo;
    }
    public String getSetfecha() {
        return setFecha;
    }

    public void setSetfecha(String setFecha) {
        this.setFecha = setFecha;
    }


}