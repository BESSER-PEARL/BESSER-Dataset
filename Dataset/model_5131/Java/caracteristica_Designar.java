





import java.util.List;
import java.util.ArrayList;

public class caracteristica_Designar extends Acao {

    private String tipoValor;
    private String valor;





    private caracteristica_Atributo caracteristica_atributo;




    private caracteristica_InconsistenciaRegraAdaptacao caracteristica_inconsistenciaregraadaptacao;


    public caracteristica_Designar(
        String tipoValor,        String valor    ) {
        super(
        );
        this.tipoValor = tipoValor;
        this.valor = valor;
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

    public caracteristica_Atributo getCaracteristica_atributo() {
        return caracteristica_atributo;
    }

    public void setCaracteristica_atributo(caracteristica_Atributo caracteristica_atributo) {
        this.caracteristica_atributo = caracteristica_atributo;
    }
    public caracteristica_InconsistenciaRegraAdaptacao getCaracteristica_inconsistenciaregraadaptacao() {
        return caracteristica_inconsistenciaregraadaptacao;
    }

    public void setCaracteristica_inconsistenciaregraadaptacao(caracteristica_InconsistenciaRegraAdaptacao caracteristica_inconsistenciaregraadaptacao) {
        this.caracteristica_inconsistenciaregraadaptacao = caracteristica_inconsistenciaregraadaptacao;
    }

}