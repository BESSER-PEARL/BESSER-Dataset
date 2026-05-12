





import java.util.List;
import java.util.ArrayList;

public class Creditos  {

    private int Numeros;





    private Materias materias;




    private List<asignacion_de_creditos> asignacion_de_creditoss;


    public Creditos(
        int Numeros    ) {
        this.Numeros = Numeros;
        this.asignacion_de_creditoss = new ArrayList<>();
    }

    public Creditos(
        int Numeros        ArrayList<asignacion_de_creditos> asignacion_de_creditoss    ) {
        this.Numeros = Numeros;
        this.asignacion_de_creditoss = asignacion_de_creditoss;
    }

    public int getNumeros() {
        return Numeros;
    }

    public void setNumeros(int Numeros) {
        this.Numeros = Numeros;
    }

    public Materias getMaterias() {
        return materias;
    }

    public void setMaterias(Materias materias) {
        this.materias = materias;
    }
    public List<asignacion_de_creditos> getAsignacion_de_creditoss() {
        return asignacion_de_creditoss;
    }

    public void addAsignacion_de_creditos(Asignacion_de_creditos asignacion_de_creditos) {
        this.asignacion_de_creditoss.add(asignacion_de_creditos);
    }

}