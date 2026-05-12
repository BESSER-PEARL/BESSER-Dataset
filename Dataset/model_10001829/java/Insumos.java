





import java.util.List;
import java.util.ArrayList;

public class Insumos  {

    private int Id_insumo;
    private String Nombre_insumo;





    private Servicios servicios;


    public Insumos(
        int Id_insumo,        String Nombre_insumo    ) {
        this.Id_insumo = Id_insumo;
        this.Nombre_insumo = Nombre_insumo;
    }


    public int getId_insumo() {
        return Id_insumo;
    }

    public void setId_insumo(int Id_insumo) {
        this.Id_insumo = Id_insumo;
    }
    public String getNombre_insumo() {
        return Nombre_insumo;
    }

    public void setNombre_insumo(String Nombre_insumo) {
        this.Nombre_insumo = Nombre_insumo;
    }

    public Servicios getServicios() {
        return servicios;
    }

    public void setServicios(Servicios servicios) {
        this.servicios = servicios;
    }

}