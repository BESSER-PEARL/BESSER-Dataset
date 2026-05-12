





import java.util.List;
import java.util.ArrayList;

public class Pemsum_Universitario  {

    private String Materias;
    private String Programa;



    public Pemsum_Universitario(
        String Materias,        String Programa    ) {
        this.Materias = Materias;
        this.Programa = Programa;
    }


    public String getMaterias() {
        return Materias;
    }

    public void setMaterias(String Materias) {
        this.Materias = Materias;
    }
    public String getPrograma() {
        return Programa;
    }

    public void setPrograma(String Programa) {
        this.Programa = Programa;
    }


}