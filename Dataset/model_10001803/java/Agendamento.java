





import java.util.List;
import java.util.ArrayList;

public class Agendamento  {

    private String Dia_e_Horario;
    private String Sede;
    private String TipoAgendamento;
    private String Especialista;
    private String Medico;





    private Consulta consulta;




    private Exame exame;


    public Agendamento(
        String Dia_e_Horario,        String Sede,        String TipoAgendamento,        String Especialista,        String Medico    ) {
        this.Dia_e_Horario = Dia_e_Horario;
        this.Sede = Sede;
        this.TipoAgendamento = TipoAgendamento;
        this.Especialista = Especialista;
        this.Medico = Medico;
    }


    public String getDia_e_horario() {
        return Dia_e_Horario;
    }

    public void setDia_e_horario(String Dia_e_Horario) {
        this.Dia_e_Horario = Dia_e_Horario;
    }
    public String getSede() {
        return Sede;
    }

    public void setSede(String Sede) {
        this.Sede = Sede;
    }
    public String getTipoagendamento() {
        return TipoAgendamento;
    }

    public void setTipoagendamento(String TipoAgendamento) {
        this.TipoAgendamento = TipoAgendamento;
    }
    public String getEspecialista() {
        return Especialista;
    }

    public void setEspecialista(String Especialista) {
        this.Especialista = Especialista;
    }
    public String getMedico() {
        return Medico;
    }

    public void setMedico(String Medico) {
        this.Medico = Medico;
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