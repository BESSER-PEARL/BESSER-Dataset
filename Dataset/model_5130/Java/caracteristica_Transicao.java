





import java.util.List;
import java.util.ArrayList;

public class caracteristica_Transicao  {

    private String etiqueta;
    private boolean safe;





    private caracteristica_Simulacao caracteristica_simulacao;




    private List<caracteristica_Acao> caracteristica_acaos;




    private List<caracteristica_RegraDeComposicao> caracteristica_regradecomposicaos;


    public caracteristica_Transicao(
        String etiqueta,        boolean safe    ) {
        this.etiqueta = etiqueta;
        this.safe = safe;
        this.caracteristica_acaos = new ArrayList<>();
        this.caracteristica_regradecomposicaos = new ArrayList<>();
    }

    public caracteristica_Transicao(
        String etiqueta,        boolean safe        ArrayList<caracteristica_Acao> caracteristica_acaos,        ArrayList<caracteristica_RegraDeComposicao> caracteristica_regradecomposicaos    ) {
        this.etiqueta = etiqueta;
        this.safe = safe;
        this.caracteristica_acaos = caracteristica_acaos;
        this.caracteristica_regradecomposicaos = caracteristica_regradecomposicaos;
    }

    public String getEtiqueta() {
        return etiqueta;
    }

    public void setEtiqueta(String etiqueta) {
        this.etiqueta = etiqueta;
    }
    public boolean getSafe() {
        return safe;
    }

    public void setSafe(boolean safe) {
        this.safe = safe;
    }

    public caracteristica_Simulacao getCaracteristica_simulacao() {
        return caracteristica_simulacao;
    }

    public void setCaracteristica_simulacao(caracteristica_Simulacao caracteristica_simulacao) {
        this.caracteristica_simulacao = caracteristica_simulacao;
    }
    public List<caracteristica_Acao> getCaracteristica_acaos() {
        return caracteristica_acaos;
    }

    public void addCaracteristica_acao(Caracteristica_acao caracteristica_acao) {
        this.caracteristica_acaos.add(caracteristica_acao);
    }
    public List<caracteristica_RegraDeComposicao> getCaracteristica_regradecomposicaos() {
        return caracteristica_regradecomposicaos;
    }

    public void addCaracteristica_regradecomposicao(Caracteristica_regradecomposicao caracteristica_regradecomposicao) {
        this.caracteristica_regradecomposicaos.add(caracteristica_regradecomposicao);
    }

}