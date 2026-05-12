





import java.util.List;
import java.util.ArrayList;

public class asignacion_de_creditos  {

    private int Cod_Materia;





    private Departamento departamento;


    public asignacion_de_creditos(
        int Cod_Materia    ) {
        this.Cod_Materia = Cod_Materia;
    }


    public int getCod_materia() {
        return Cod_Materia;
    }

    public void setCod_materia(int Cod_Materia) {
        this.Cod_Materia = Cod_Materia;
    }

    public Departamento getDepartamento() {
        return departamento;
    }

    public void setDepartamento(Departamento departamento) {
        this.departamento = departamento;
    }

}