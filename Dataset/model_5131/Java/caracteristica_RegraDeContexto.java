





import java.util.List;
import java.util.ArrayList;

public class caracteristica_RegraDeContexto extends Regra {






    private caracteristica_Evento caracteristica_evento;




    private caracteristica_InconsistenciaRegraAdaptacao caracteristica_inconsistenciaregraadaptacao;




    private caracteristica_Acao caracteristica_acao;


    public caracteristica_RegraDeContexto(
    ) {
        super(
        );
    }



    public caracteristica_Evento getCaracteristica_evento() {
        return caracteristica_evento;
    }

    public void setCaracteristica_evento(caracteristica_Evento caracteristica_evento) {
        this.caracteristica_evento = caracteristica_evento;
    }
    public caracteristica_InconsistenciaRegraAdaptacao getCaracteristica_inconsistenciaregraadaptacao() {
        return caracteristica_inconsistenciaregraadaptacao;
    }

    public void setCaracteristica_inconsistenciaregraadaptacao(caracteristica_InconsistenciaRegraAdaptacao caracteristica_inconsistenciaregraadaptacao) {
        this.caracteristica_inconsistenciaregraadaptacao = caracteristica_inconsistenciaregraadaptacao;
    }
    public caracteristica_Acao getCaracteristica_acao() {
        return caracteristica_acao;
    }

    public void setCaracteristica_acao(caracteristica_Acao caracteristica_acao) {
        this.caracteristica_acao = caracteristica_acao;
    }

}