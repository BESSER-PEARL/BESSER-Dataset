





import java.util.List;
import java.util.ArrayList;

public class clinicasaudeperfeita_Medicamento  {

    private String nome;





    private clinicasaudeperfeita_Consulta clinicasaudeperfeita_consulta;


    public clinicasaudeperfeita_Medicamento(
        String nome    ) {
        this.nome = nome;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public clinicasaudeperfeita_Consulta getClinicasaudeperfeita_consulta() {
        return clinicasaudeperfeita_consulta;
    }

    public void setClinicasaudeperfeita_consulta(clinicasaudeperfeita_Consulta clinicasaudeperfeita_consulta) {
        this.clinicasaudeperfeita_consulta = clinicasaudeperfeita_consulta;
    }

}