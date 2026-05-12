





import java.util.List;
import java.util.ArrayList;

public class Racun  {

    private int RacunID;
    private None Iznos;
    private boolean Placeno;





    private Rezervacija rezervacija;


    public Racun(
        int RacunID,        None Iznos,        boolean Placeno    ) {
        this.RacunID = RacunID;
        this.Iznos = Iznos;
        this.Placeno = Placeno;
    }


    public int getRacunid() {
        return RacunID;
    }

    public void setRacunid(int RacunID) {
        this.RacunID = RacunID;
    }
    public None getIznos() {
        return Iznos;
    }

    public void setIznos(None Iznos) {
        this.Iznos = Iznos;
    }
    public boolean getPlaceno() {
        return Placeno;
    }

    public void setPlaceno(boolean Placeno) {
        this.Placeno = Placeno;
    }

    public Rezervacija getRezervacija() {
        return rezervacija;
    }

    public void setRezervacija(Rezervacija rezervacija) {
        this.rezervacija = rezervacija;
    }

}