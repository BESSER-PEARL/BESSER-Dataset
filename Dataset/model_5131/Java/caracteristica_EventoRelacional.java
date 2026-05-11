





import java.util.List;
import java.util.ArrayList;

public class caracteristica_EventoRelacional extends Evento {

    private String operadorRelacional;
    private String valor;





    private caracteristica_InformacaoDeContexto caracteristica_informacaodecontexto;


    public caracteristica_EventoRelacional(
        String operadorRelacional,        String valor    ) {
        super(
        );
        this.operadorRelacional = operadorRelacional;
        this.valor = valor;
    }


    public String getOperadorrelacional() {
        return operadorRelacional;
    }

    public void setOperadorrelacional(String operadorRelacional) {
        this.operadorRelacional = operadorRelacional;
    }
    public String getValor() {
        return valor;
    }

    public void setValor(String valor) {
        this.valor = valor;
    }

    public caracteristica_InformacaoDeContexto getCaracteristica_informacaodecontexto() {
        return caracteristica_informacaodecontexto;
    }

    public void setCaracteristica_informacaodecontexto(caracteristica_InformacaoDeContexto caracteristica_informacaodecontexto) {
        this.caracteristica_informacaodecontexto = caracteristica_informacaodecontexto;
    }

}