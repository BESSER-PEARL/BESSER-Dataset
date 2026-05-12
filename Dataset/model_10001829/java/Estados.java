





import java.util.List;
import java.util.ArrayList;

public class Estados  {

    private int id_estados;
    private String Nombre_estados;





    private Mascotas mascotas;


    public Estados(
        int id_estados,        String Nombre_estados    ) {
        this.id_estados = id_estados;
        this.Nombre_estados = Nombre_estados;
    }


    public int getId_estados() {
        return id_estados;
    }

    public void setId_estados(int id_estados) {
        this.id_estados = id_estados;
    }
    public String getNombre_estados() {
        return Nombre_estados;
    }

    public void setNombre_estados(String Nombre_estados) {
        this.Nombre_estados = Nombre_estados;
    }

    public Mascotas getMascotas() {
        return mascotas;
    }

    public void setMascotas(Mascotas mascotas) {
        this.mascotas = mascotas;
    }

}