





import java.util.List;
import java.util.ArrayList;

public class caracteristica_LiteralAcao extends Acao {

    private String presenca;





    private caracteristica_InconsistenciaRegraAdaptacao caracteristica_inconsistenciaregraadaptacao;




    private caracteristica_ElementoCaracteristico caracteristica_elementocaracteristico;


    public caracteristica_LiteralAcao(
        String presenca    ) {
        super(
        );
        this.presenca = presenca;
    }


    public String getPresenca() {
        return presenca;
    }

    public void setPresenca(String presenca) {
        this.presenca = presenca;
    }

    public caracteristica_InconsistenciaRegraAdaptacao getCaracteristica_inconsistenciaregraadaptacao() {
        return caracteristica_inconsistenciaregraadaptacao;
    }

    public void setCaracteristica_inconsistenciaregraadaptacao(caracteristica_InconsistenciaRegraAdaptacao caracteristica_inconsistenciaregraadaptacao) {
        this.caracteristica_inconsistenciaregraadaptacao = caracteristica_inconsistenciaregraadaptacao;
    }
    public caracteristica_ElementoCaracteristico getCaracteristica_elementocaracteristico() {
        return caracteristica_elementocaracteristico;
    }

    public void setCaracteristica_elementocaracteristico(caracteristica_ElementoCaracteristico caracteristica_elementocaracteristico) {
        this.caracteristica_elementocaracteristico = caracteristica_elementocaracteristico;
    }

}