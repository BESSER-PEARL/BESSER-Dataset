





import java.util.List;
import java.util.ArrayList;

public class Jornada  {

    private None Dinero_en_caja;
    private String Stock;
    private None Arqueo;





    private List<Producto> productos;




    private Supervisor supervisor;


    public Jornada(
        None Dinero_en_caja,        String Stock,        None Arqueo    ) {
        this.Dinero_en_caja = Dinero_en_caja;
        this.Stock = Stock;
        this.Arqueo = Arqueo;
        this.productos = new ArrayList<>();
    }

    public Jornada(
        None Dinero_en_caja,        String Stock,        None Arqueo        ArrayList<Producto> productos    ) {
        this.Dinero_en_caja = Dinero_en_caja;
        this.Stock = Stock;
        this.Arqueo = Arqueo;
        this.productos = productos;
    }

    public None getDinero_en_caja() {
        return Dinero_en_caja;
    }

    public void setDinero_en_caja(None Dinero_en_caja) {
        this.Dinero_en_caja = Dinero_en_caja;
    }
    public String getStock() {
        return Stock;
    }

    public void setStock(String Stock) {
        this.Stock = Stock;
    }
    public None getArqueo() {
        return Arqueo;
    }

    public void setArqueo(None Arqueo) {
        this.Arqueo = Arqueo;
    }

    public List<Producto> getProductos() {
        return productos;
    }

    public void addProducto(Producto producto) {
        this.productos.add(producto);
    }
    public Supervisor getSupervisor() {
        return supervisor;
    }

    public void setSupervisor(Supervisor supervisor) {
        this.supervisor = supervisor;
    }

}