





import java.util.List;
import java.util.ArrayList;

public class ventas  {

    private String valordeventa;
    private String fechadeventas;





    private Comerciales comerciales;


    public ventas(
        String valordeventa,        String fechadeventas    ) {
        this.valordeventa = valordeventa;
        this.fechadeventas = fechadeventas;
    }


    public String getValordeventa() {
        return valordeventa;
    }

    public void setValordeventa(String valordeventa) {
        this.valordeventa = valordeventa;
    }
    public String getFechadeventas() {
        return fechadeventas;
    }

    public void setFechadeventas(String fechadeventas) {
        this.fechadeventas = fechadeventas;
    }

    public Comerciales getComerciales() {
        return comerciales;
    }

    public void setComerciales(Comerciales comerciales) {
        this.comerciales = comerciales;
    }

}