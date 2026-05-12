





import java.util.List;
import java.util.ArrayList;

public class Tipo_mascota  {

    private String Nombre_Tipo;
    private int id_Tipo_Mascota;





    private List<Mascotas> mascotass;


    public Tipo_mascota(
        String Nombre_Tipo,        int id_Tipo_Mascota    ) {
        this.Nombre_Tipo = Nombre_Tipo;
        this.id_Tipo_Mascota = id_Tipo_Mascota;
        this.mascotass = new ArrayList<>();
    }

    public Tipo_mascota(
        String Nombre_Tipo,        int id_Tipo_Mascota        ArrayList<Mascotas> mascotass    ) {
        this.Nombre_Tipo = Nombre_Tipo;
        this.id_Tipo_Mascota = id_Tipo_Mascota;
        this.mascotass = mascotass;
    }

    public String getNombre_tipo() {
        return Nombre_Tipo;
    }

    public void setNombre_tipo(String Nombre_Tipo) {
        this.Nombre_Tipo = Nombre_Tipo;
    }
    public int getId_tipo_mascota() {
        return id_Tipo_Mascota;
    }

    public void setId_tipo_mascota(int id_Tipo_Mascota) {
        this.id_Tipo_Mascota = id_Tipo_Mascota;
    }

    public List<Mascotas> getMascotass() {
        return mascotass;
    }

    public void addMascotas(Mascotas mascotas) {
        this.mascotass.add(mascotas);
    }

}