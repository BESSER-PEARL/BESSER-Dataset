





import java.util.List;
import java.util.ArrayList;

public class Comerciales  {

    private String Zona;
    private String Nombre;
    private String Id;





    private Presupuesto presupuesto;




    private Facturas facturas;


    public Comerciales(
        String Zona,        String Nombre,        String Id    ) {
        this.Zona = Zona;
        this.Nombre = Nombre;
        this.Id = Id;
    }


    public String getZona() {
        return Zona;
    }

    public void setZona(String Zona) {
        this.Zona = Zona;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }

    public Presupuesto getPresupuesto() {
        return presupuesto;
    }

    public void setPresupuesto(Presupuesto presupuesto) {
        this.presupuesto = presupuesto;
    }
    public Facturas getFacturas() {
        return facturas;
    }

    public void setFacturas(Facturas facturas) {
        this.facturas = facturas;
    }

}