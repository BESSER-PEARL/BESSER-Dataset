





import java.util.List;
import java.util.ArrayList;

public class Consulta  {

    private String data;
    private String pre_o;





    private Medico medico;




    private Paciente paciente;


    public Consulta(
        String data,        String pre_o    ) {
        this.data = data;
        this.pre_o = pre_o;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getPre_o() {
        return pre_o;
    }

    public void setPre_o(String pre_o) {
        this.pre_o = pre_o;
    }

    public Medico getMedico() {
        return medico;
    }

    public void setMedico(Medico medico) {
        this.medico = medico;
    }
    public Paciente getPaciente() {
        return paciente;
    }

    public void setPaciente(Paciente paciente) {
        this.paciente = paciente;
    }

}