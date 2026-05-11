





import java.util.List;
import java.util.ArrayList;

public class caracteristica_InformacaoDeContexto extends Elemento {

    private String qualidade;
    private String validade;
    private String tipoValor;
    private String valor;
    private String origem;



    public caracteristica_InformacaoDeContexto(
        String qualidade,        String validade,        String tipoValor,        String valor,        String origem    ) {
        super(
        );
        this.qualidade = qualidade;
        this.validade = validade;
        this.tipoValor = tipoValor;
        this.valor = valor;
        this.origem = origem;
    }


    public String getQualidade() {
        return qualidade;
    }

    public void setQualidade(String qualidade) {
        this.qualidade = qualidade;
    }
    public String getValidade() {
        return validade;
    }

    public void setValidade(String validade) {
        this.validade = validade;
    }
    public String getTipovalor() {
        return tipoValor;
    }

    public void setTipovalor(String tipoValor) {
        this.tipoValor = tipoValor;
    }
    public String getValor() {
        return valor;
    }

    public void setValor(String valor) {
        this.valor = valor;
    }
    public String getOrigem() {
        return origem;
    }

    public void setOrigem(String origem) {
        this.origem = origem;
    }


}