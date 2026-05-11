





import java.util.List;
import java.util.ArrayList;

public class caracteristica_Designar extends Acao {

    private String valor;
    private String tipoValor;





    private caracteristica_InconsistenciaRegraAdaptacao caracteristica_inconsistenciaregraadaptacao;




    private caracteristica_Atributo caracteristica_atributo;


    public caracteristica_Designar(
        String valor,        String tipoValor    ) {
        super(
        );
        this.valor = valor;
        this.tipoValor = tipoValor;
    }


    public String getValor() {
        return valor;
    }

    public void setValor(String valor) {
        this.valor = valor;
    }
    public String getTipovalor() {
        return tipoValor;
    }

    public void setTipovalor(String tipoValor) {
        this.tipoValor = tipoValor;
    }

    public caracteristica_InconsistenciaRegraAdaptacao getCaracteristica_inconsistenciaregraadaptacao() {
        return caracteristica_inconsistenciaregraadaptacao;
    }

    public void setCaracteristica_inconsistenciaregraadaptacao(caracteristica_InconsistenciaRegraAdaptacao caracteristica_inconsistenciaregraadaptacao) {
        this.caracteristica_inconsistenciaregraadaptacao = caracteristica_inconsistenciaregraadaptacao;
    }
    public caracteristica_Atributo getCaracteristica_atributo() {
        return caracteristica_atributo;
    }

    public void setCaracteristica_atributo(caracteristica_Atributo caracteristica_atributo) {
        this.caracteristica_atributo = caracteristica_atributo;
    }

}