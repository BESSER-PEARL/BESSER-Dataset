





import java.util.List;
import java.util.ArrayList;

public class TipoDeEvento  {

    private String Evento;
    private String Cod_TipodeEvento;



    public TipoDeEvento(
        String Evento,        String Cod_TipodeEvento    ) {
        this.Evento = Evento;
        this.Cod_TipodeEvento = Cod_TipodeEvento;
    }


    public String getEvento() {
        return Evento;
    }

    public void setEvento(String Evento) {
        this.Evento = Evento;
    }
    public String getCod_tipodeevento() {
        return Cod_TipodeEvento;
    }

    public void setCod_tipodeevento(String Cod_TipodeEvento) {
        this.Cod_TipodeEvento = Cod_TipodeEvento;
    }


}