





import java.util.List;
import java.util.ArrayList;

public class Asistencia  {

    private String Sucursal;
    private String Ingreso;





    private List<Cliente1> cliente1s;


    public Asistencia(
        String Sucursal,        String Ingreso    ) {
        this.Sucursal = Sucursal;
        this.Ingreso = Ingreso;
        this.cliente1s = new ArrayList<>();
    }

    public Asistencia(
        String Sucursal,        String Ingreso        ArrayList<Cliente1> cliente1s    ) {
        this.Sucursal = Sucursal;
        this.Ingreso = Ingreso;
        this.cliente1s = cliente1s;
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

    public List<Cliente1> getCliente1s() {
        return cliente1s;
    }

    public void addCliente1(Cliente1 cliente1) {
        this.cliente1s.add(cliente1);
    }

}