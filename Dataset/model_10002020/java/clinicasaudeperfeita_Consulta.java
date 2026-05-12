





import java.util.List;
import java.util.ArrayList;

public class clinicasaudeperfeita_Consulta  {

    private String problemasPaciente;
    private String data;
    private None exame;
    private None medico;
    private String orientacoesMedicas;
    private String hora;
    private None paciente;
    private None medicamentos;
    private boolean realizada;
    private boolean marcada;





    private clinicasaudeperfeita_Paciente clinicasaudeperfeita_paciente;


    public clinicasaudeperfeita_Consulta(
        String problemasPaciente,        String data,        None exame,        None medico,        String orientacoesMedicas,        String hora,        None paciente,        None medicamentos,        boolean realizada,        boolean marcada    ) {
        this.problemasPaciente = problemasPaciente;
        this.data = data;
        this.exame = exame;
        this.medico = medico;
        this.orientacoesMedicas = orientacoesMedicas;
        this.hora = hora;
        this.paciente = paciente;
        this.medicamentos = medicamentos;
        this.realizada = realizada;
        this.marcada = marcada;
    }


    public String getProblemaspaciente() {
        return problemasPaciente;
    }

    public void setProblemaspaciente(String problemasPaciente) {
        this.problemasPaciente = problemasPaciente;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public None getExame() {
        return exame;
    }

    public void setExame(None exame) {
        this.exame = exame;
    }
    public None getMedico() {
        return medico;
    }

    public void setMedico(None medico) {
        this.medico = medico;
    }
    public String getOrientacoesmedicas() {
        return orientacoesMedicas;
    }

    public void setOrientacoesmedicas(String orientacoesMedicas) {
        this.orientacoesMedicas = orientacoesMedicas;
    }
    public String getHora() {
        return hora;
    }

    public void setHora(String hora) {
        this.hora = hora;
    }
    public None getPaciente() {
        return paciente;
    }

    public void setPaciente(None paciente) {
        this.paciente = paciente;
    }
    public None getMedicamentos() {
        return medicamentos;
    }

    public void setMedicamentos(None medicamentos) {
        this.medicamentos = medicamentos;
    }
    public boolean getRealizada() {
        return realizada;
    }

    public void setRealizada(boolean realizada) {
        this.realizada = realizada;
    }
    public boolean getMarcada() {
        return marcada;
    }

    public void setMarcada(boolean marcada) {
        this.marcada = marcada;
    }

    public clinicasaudeperfeita_Paciente getClinicasaudeperfeita_paciente() {
        return clinicasaudeperfeita_paciente;
    }

    public void setClinicasaudeperfeita_paciente(clinicasaudeperfeita_Paciente clinicasaudeperfeita_paciente) {
        this.clinicasaudeperfeita_paciente = clinicasaudeperfeita_paciente;
    }

}