





import java.util.List;
import java.util.ArrayList;

public class Mensagem  {

    private String mensagem;
    private String assunto;
    private String dataEnvio;
    private boolean geral;





    private ProfissionalSaude profissionalsaude;




    private List<Interacao> interacaos;




    private Paciente paciente;


    public Mensagem(
        String mensagem,        String assunto,        String dataEnvio,        boolean geral    ) {
        this.mensagem = mensagem;
        this.assunto = assunto;
        this.dataEnvio = dataEnvio;
        this.geral = geral;
        this.interacaos = new ArrayList<>();
    }

    public Mensagem(
        String mensagem,        String assunto,        String dataEnvio,        boolean geral        ArrayList<Interacao> interacaos    ) {
        this.mensagem = mensagem;
        this.assunto = assunto;
        this.dataEnvio = dataEnvio;
        this.geral = geral;
        this.interacaos = interacaos;
    }

    public String getMensagem() {
        return mensagem;
    }

    public void setMensagem(String mensagem) {
        this.mensagem = mensagem;
    }
    public String getAssunto() {
        return assunto;
    }

    public void setAssunto(String assunto) {
        this.assunto = assunto;
    }
    public String getDataenvio() {
        return dataEnvio;
    }

    public void setDataenvio(String dataEnvio) {
        this.dataEnvio = dataEnvio;
    }
    public boolean getGeral() {
        return geral;
    }

    public void setGeral(boolean geral) {
        this.geral = geral;
    }

    public ProfissionalSaude getProfissionalsaude() {
        return profissionalsaude;
    }

    public void setProfissionalsaude(ProfissionalSaude profissionalsaude) {
        this.profissionalsaude = profissionalsaude;
    }
    public List<Interacao> getInteracaos() {
        return interacaos;
    }

    public void addInteracao(Interacao interacao) {
        this.interacaos.add(interacao);
    }
    public Paciente getPaciente() {
        return paciente;
    }

    public void setPaciente(Paciente paciente) {
        this.paciente = paciente;
    }

}