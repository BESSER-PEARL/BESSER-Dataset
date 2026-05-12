





import java.util.List;
import java.util.ArrayList;

public class Aranzman  {

    private int DestinacijaID;
    private int BrojMesta;
    private int AranzmanID;
    private boolean Popunjeno;
    private None Cena;
    private int TerminID;
    private String NazivAranzmana;





    private Rezervacija rezervacija;


    public Aranzman(
        int DestinacijaID,        int BrojMesta,        int AranzmanID,        boolean Popunjeno,        None Cena,        int TerminID,        String NazivAranzmana    ) {
        this.DestinacijaID = DestinacijaID;
        this.BrojMesta = BrojMesta;
        this.AranzmanID = AranzmanID;
        this.Popunjeno = Popunjeno;
        this.Cena = Cena;
        this.TerminID = TerminID;
        this.NazivAranzmana = NazivAranzmana;
    }


    public int getDestinacijaid() {
        return DestinacijaID;
    }

    public void setDestinacijaid(int DestinacijaID) {
        this.DestinacijaID = DestinacijaID;
    }
    public int getBrojmesta() {
        return BrojMesta;
    }

    public void setBrojmesta(int BrojMesta) {
        this.BrojMesta = BrojMesta;
    }
    public int getAranzmanid() {
        return AranzmanID;
    }

    public void setAranzmanid(int AranzmanID) {
        this.AranzmanID = AranzmanID;
    }
    public boolean getPopunjeno() {
        return Popunjeno;
    }

    public void setPopunjeno(boolean Popunjeno) {
        this.Popunjeno = Popunjeno;
    }
    public None getCena() {
        return Cena;
    }

    public void setCena(None Cena) {
        this.Cena = Cena;
    }
    public int getTerminid() {
        return TerminID;
    }

    public void setTerminid(int TerminID) {
        this.TerminID = TerminID;
    }
    public String getNazivaranzmana() {
        return NazivAranzmana;
    }

    public void setNazivaranzmana(String NazivAranzmana) {
        this.NazivAranzmana = NazivAranzmana;
    }

    public Rezervacija getRezervacija() {
        return rezervacija;
    }

    public void setRezervacija(Rezervacija rezervacija) {
        this.rezervacija = rezervacija;
    }

}