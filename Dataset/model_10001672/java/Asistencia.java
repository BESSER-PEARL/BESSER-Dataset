





import java.util.List;
import java.util.ArrayList;

public class Asistencia  {

    private String Sucursal;
    private String Ingreso;





    private Cliente1 cliente1;


    public Asistencia(
        String Sucursal,        String Ingreso    ) {
        this.Sucursal = Sucursal;
        this.Ingreso = Ingreso;
    }


    public String getSucursal() {
        return Sucursal;
    }

    public void setSucursal(String Sucursal) {
        this.Sucursal = Sucursal;
    }
    public String getIngreso() {
        return Ingreso;
    }

    public void setIngreso(String Ingreso) {
        this.Ingreso = Ingreso;
    }

    public Cliente1 getCliente1() {
        return cliente1;
    }

    public void setCliente1(Cliente1 cliente1) {
        this.cliente1 = cliente1;
    }

}