





import java.util.List;
import java.util.ArrayList;

public class Horas_de_clase  {

    private String CreditosMateria;
    private String TipoCreditos;





    private Materias materias;


    public Horas_de_clase(
        String CreditosMateria,        String TipoCreditos    ) {
        this.CreditosMateria = CreditosMateria;
        this.TipoCreditos = TipoCreditos;
    }


    public String getCreditosmateria() {
        return CreditosMateria;
    }

    public void setCreditosmateria(String CreditosMateria) {
        this.CreditosMateria = CreditosMateria;
    }
    public String getTipocreditos() {
        return TipoCreditos;
    }

    public void setTipocreditos(String TipoCreditos) {
        this.TipoCreditos = TipoCreditos;
    }

    public Materias getMaterias() {
        return materias;
    }

    public void setMaterias(Materias materias) {
        this.materias = materias;
    }

}