





import java.util.List;
import java.util.ArrayList;

public class Entlehnausweis  {

    private String g_ltigKeitsDatum;
    private int id;





    private Kunde kunde;


    public Entlehnausweis(
        String g_ltigKeitsDatum,        int id    ) {
        this.g_ltigKeitsDatum = g_ltigKeitsDatum;
        this.id = id;
    }


    public String getG_ltigkeitsdatum() {
        return g_ltigKeitsDatum;
    }

    public void setG_ltigkeitsdatum(String g_ltigKeitsDatum) {
        this.g_ltigKeitsDatum = g_ltigKeitsDatum;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Kunde getKunde() {
        return kunde;
    }

    public void setKunde(Kunde kunde) {
        this.kunde = kunde;
    }

}