





import java.util.List;
import java.util.ArrayList;

public class caracteristica_InformacaoDeContexto extends Elemento {

    private String valor;
    private String validade;
    private String qualidade;
    private String tipoValor;
    private String origem;





    private caracteristica_EntidadeDeContexto caracteristica_entidadedecontexto;




    private caracteristica_EntidadeDeContexto caracteristica_entidadedecontexto;


    public caracteristica_InformacaoDeContexto(
        String valor,        String validade,        String qualidade,        String tipoValor,        String origem    ) {
        super(
        );
        this.valor = valor;
        this.validade = validade;
        this.qualidade = qualidade;
        this.tipoValor = tipoValor;
        this.origem = origem;
    }


    public String getValor() {
        return valor;
    }

    public void setValor(String valor) {
        this.valor = valor;
    }
    public String getValidade() {
        return validade;
    }

    public void setValidade(String validade) {
        this.validade = validade;
    }
    public String getQualidade() {
        return qualidade;
    }

    public void setQualidade(String qualidade) {
        this.qualidade = qualidade;
    }
    public String getTipovalor() {
        return tipoValor;
    }

    public void setTipovalor(String tipoValor) {
        this.tipoValor = tipoValor;
    }
    public String getOrigem() {
        return origem;
    }

    public void setOrigem(String origem) {
        this.origem = origem;
    }

    public caracteristica_EntidadeDeContexto getCaracteristica_entidadedecontexto() {
        return caracteristica_entidadedecontexto;
    }

    public void setCaracteristica_entidadedecontexto(caracteristica_EntidadeDeContexto caracteristica_entidadedecontexto) {
        this.caracteristica_entidadedecontexto = caracteristica_entidadedecontexto;
    }
    public caracteristica_EntidadeDeContexto getCaracteristica_entidadedecontexto() {
        return caracteristica_entidadedecontexto;
    }

    public void setCaracteristica_entidadedecontexto(caracteristica_EntidadeDeContexto caracteristica_entidadedecontexto) {
        this.caracteristica_entidadedecontexto = caracteristica_entidadedecontexto;
    }

}