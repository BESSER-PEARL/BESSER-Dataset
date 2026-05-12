





import java.util.List;
import java.util.ArrayList;

public class ConsultaExame  {

    private boolean Entregue;





    private Consulta consulta;




    private Exame exame;


    public ConsultaExame(
        boolean Entregue    ) {
        this.Entregue = Entregue;
    }


    public boolean getEntregue() {
        return Entregue;
    }

    public void setEntregue(boolean Entregue) {
        this.Entregue = Entregue;
    }

    public Consulta getConsulta() {
        return consulta;
    }

    public void setConsulta(Consulta consulta) {
        this.consulta = consulta;
    }
    public Exame getExame() {
        return exame;
    }

    public void setExame(Exame exame) {
        this.exame = exame;
    }

}