





import java.util.List;
import java.util.ArrayList;

public class TreinoMonitoramento  {

    private String fim;
    private String inicio;



    public TreinoMonitoramento(
        String fim,        String inicio    ) {
        this.fim = fim;
        this.inicio = inicio;
    }


    public String getFim() {
        return fim;
    }

    public void setFim(String fim) {
        this.fim = fim;
    }
    public String getInicio() {
        return inicio;
    }

    public void setInicio(String inicio) {
        this.inicio = inicio;
    }


}