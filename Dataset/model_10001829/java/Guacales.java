





import java.util.List;
import java.util.ArrayList;

public class Guacales  {

    private int Id_guacal;





    private Mascotas mascotas;


    public Guacales(
        int Id_guacal    ) {
        this.Id_guacal = Id_guacal;
    }


    public int getId_guacal() {
        return Id_guacal;
    }

    public void setId_guacal(int Id_guacal) {
        this.Id_guacal = Id_guacal;
    }

    public Mascotas getMascotas() {
        return mascotas;
    }

    public void setMascotas(Mascotas mascotas) {
        this.mascotas = mascotas;
    }

}