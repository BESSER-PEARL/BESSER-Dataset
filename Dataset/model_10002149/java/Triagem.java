





import java.util.List;
import java.util.ArrayList;

public class Triagem  {

    private None paciente;
    private String altura;
    private None pressao;
    private String IMC;
    private String peso;
    private String alergias;
    private boolean febre;
    private None enfermeira;
    private String sintoma;
    private String temperatura;





    private Paciente paciente;




    private Enfermeira enfermeira;


    public Triagem(
        None paciente,        String altura,        None pressao,        String IMC,        String peso,        String alergias,        boolean febre,        None enfermeira,        String sintoma,        String temperatura    ) {
        this.paciente = paciente;
        this.altura = altura;
        this.pressao = pressao;
        this.IMC = IMC;
        this.peso = peso;
        this.alergias = alergias;
        this.febre = febre;
        this.enfermeira = enfermeira;
        this.sintoma = sintoma;
        this.temperatura = temperatura;
    }


    public None getPaciente() {
        return paciente;
    }

    public void setPaciente(None paciente) {
        this.paciente = paciente;
    }
    public String getAltura() {
        return altura;
    }

    public void setAltura(String altura) {
        this.altura = altura;
    }
    public None getPressao() {
        return pressao;
    }

    public void setPressao(None pressao) {
        this.pressao = pressao;
    }
    public String getImc() {
        return IMC;
    }

    public void setImc(String IMC) {
        this.IMC = IMC;
    }
    public String getPeso() {
        return peso;
    }

    public void setPeso(String peso) {
        this.peso = peso;
    }
    public String getAlergias() {
        return alergias;
    }

    public void setAlergias(String alergias) {
        this.alergias = alergias;
    }
    public boolean getFebre() {
        return febre;
    }

    public void setFebre(boolean febre) {
        this.febre = febre;
    }
    public None getEnfermeira() {
        return enfermeira;
    }

    public void setEnfermeira(None enfermeira) {
        this.enfermeira = enfermeira;
    }
    public String getSintoma() {
        return sintoma;
    }

    public void setSintoma(String sintoma) {
        this.sintoma = sintoma;
    }
    public String getTemperatura() {
        return temperatura;
    }

    public void setTemperatura(String temperatura) {
        this.temperatura = temperatura;
    }

    public Paciente getPaciente() {
        return paciente;
    }

    public void setPaciente(Paciente paciente) {
        this.paciente = paciente;
    }
    public Enfermeira getEnfermeira() {
        return enfermeira;
    }

    public void setEnfermeira(Enfermeira enfermeira) {
        this.enfermeira = enfermeira;
    }

}