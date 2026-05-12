





import java.util.List;
import java.util.ArrayList;

public class Pedido_Exame  {

    private int codigo;





    private Paciente paciente;


    public Pedido_Exame(
        int codigo    ) {
        this.codigo = codigo;
    }


    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public Paciente getPaciente() {
        return paciente;
    }

    public void setPaciente(Paciente paciente) {
        this.paciente = paciente;
    }

}