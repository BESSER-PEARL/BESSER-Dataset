





import java.util.List;
import java.util.ArrayList;

public class Mascotas  {

    private int Id_mascota;
    private None tipo_mascota;





    private List<Servicios> servicioss;


    public Mascotas(
        int Id_mascota,        None tipo_mascota    ) {
        this.Id_mascota = Id_mascota;
        this.tipo_mascota = tipo_mascota;
        this.servicioss = new ArrayList<>();
    }

    public Mascotas(
        int Id_mascota,        None tipo_mascota        ArrayList<Servicios> servicioss    ) {
        this.Id_mascota = Id_mascota;
        this.tipo_mascota = tipo_mascota;
        this.servicioss = servicioss;
    }

    public int getId_mascota() {
        return Id_mascota;
    }

    public void setId_mascota(int Id_mascota) {
        this.Id_mascota = Id_mascota;
    }
    public None getTipo_mascota() {
        return tipo_mascota;
    }

    public void setTipo_mascota(None tipo_mascota) {
        this.tipo_mascota = tipo_mascota;
    }

    public List<Servicios> getServicioss() {
        return servicioss;
    }

    public void addServicios(Servicios servicios) {
        this.servicioss.add(servicios);
    }

}