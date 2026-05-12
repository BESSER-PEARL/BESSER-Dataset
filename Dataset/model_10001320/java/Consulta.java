





import java.util.List;
import java.util.ArrayList;

public class Consulta  {

    private None MedicoId;
    private String DataHora;
    private None PacienteId;
    private String Queixas;





    private Paciente paciente;


    public Consulta(
        None MedicoId,        String DataHora,        None PacienteId,        String Queixas    ) {
        this.MedicoId = MedicoId;
        this.DataHora = DataHora;
        this.PacienteId = PacienteId;
        this.Queixas = Queixas;
    }


    public None getMedicoid() {
        return MedicoId;
    }

    public void setMedicoid(None MedicoId) {
        this.MedicoId = MedicoId;
    }
    public String getDatahora() {
        return DataHora;
    }

    public void setDatahora(String DataHora) {
        this.DataHora = DataHora;
    }
    public None getPacienteid() {
        return PacienteId;
    }

    public void setPacienteid(None PacienteId) {
        this.PacienteId = PacienteId;
    }
    public String getQueixas() {
        return Queixas;
    }

    public void setQueixas(String Queixas) {
        this.Queixas = Queixas;
    }

    public Paciente getPaciente() {
        return paciente;
    }

    public void setPaciente(Paciente paciente) {
        this.paciente = paciente;
    }

}