





import java.util.List;
import java.util.ArrayList;

public class TipoCuenta  {

    private int id;
    private String tipo;
    private boolean estado;





    private List<Cuenta_external> cuenta_externals;


    public TipoCuenta(
        int id,        String tipo,        boolean estado    ) {
        this.id = id;
        this.tipo = tipo;
        this.estado = estado;
        this.cuenta_externals = new ArrayList<>();
    }

    public TipoCuenta(
        int id,        String tipo,        boolean estado        ArrayList<Cuenta_external> cuenta_externals    ) {
        this.id = id;
        this.tipo = tipo;
        this.estado = estado;
        this.cuenta_externals = cuenta_externals;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public boolean getEstado() {
        return estado;
    }

    public void setEstado(boolean estado) {
        this.estado = estado;
    }

    public List<Cuenta_external> getCuenta_externals() {
        return cuenta_externals;
    }

    public void addCuenta_external(Cuenta_external cuenta_external) {
        this.cuenta_externals.add(cuenta_external);
    }

}