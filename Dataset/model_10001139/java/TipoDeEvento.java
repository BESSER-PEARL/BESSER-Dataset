





import java.util.List;
import java.util.ArrayList;

public class TipoDeEvento  {

    private String Cod_TipodeEvento;
    private String Evento;





    private List<Evento> eventos;


    public TipoDeEvento(
        String Cod_TipodeEvento,        String Evento    ) {
        this.Cod_TipodeEvento = Cod_TipodeEvento;
        this.Evento = Evento;
        this.eventos = new ArrayList<>();
    }

    public TipoDeEvento(
        String Cod_TipodeEvento,        String Evento        ArrayList<Evento> eventos    ) {
        this.Cod_TipodeEvento = Cod_TipodeEvento;
        this.Evento = Evento;
        this.eventos = eventos;
    }

    public String getCod_tipodeevento() {
        return Cod_TipodeEvento;
    }

    public void setCod_tipodeevento(String Cod_TipodeEvento) {
        this.Cod_TipodeEvento = Cod_TipodeEvento;
    }
    public String getEvento() {
        return Evento;
    }

    public void setEvento(String Evento) {
        this.Evento = Evento;
    }

    public List<Evento> getEventos() {
        return eventos;
    }

    public void addEvento(Evento evento) {
        this.eventos.add(evento);
    }

}