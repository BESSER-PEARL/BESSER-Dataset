





import java.util.List;
import java.util.ArrayList;

public class Departamento  {

    private int ID_Profesores;





    private Pemsum_Universitario pemsum_universitario;


    public Departamento(
        int ID_Profesores    ) {
        this.ID_Profesores = ID_Profesores;
    }


    public int getId_profesores() {
        return ID_Profesores;
    }

    public void setId_profesores(int ID_Profesores) {
        this.ID_Profesores = ID_Profesores;
    }

    public Pemsum_Universitario getPemsum_universitario() {
        return pemsum_universitario;
    }

    public void setPemsum_universitario(Pemsum_Universitario pemsum_universitario) {
        this.pemsum_universitario = pemsum_universitario;
    }

}