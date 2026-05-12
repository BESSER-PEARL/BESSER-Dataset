





import java.util.List;
import java.util.ArrayList;

public class Rezervisanje  {

    private String Cena;
    private String DatumDolaska;
    private int DestiID;
    private boolean SlobMesto;
    private int KorisnikID;
    private int RezerID;
    private String DatumPolaska;
    private int PutnikID;





    private List<Karta> kartas;




    private Destinacija destinacija;




    private Korisnik_IS korisnik_is;


    public Rezervisanje(
        String Cena,        String DatumDolaska,        int DestiID,        boolean SlobMesto,        int KorisnikID,        int RezerID,        String DatumPolaska,        int PutnikID    ) {
        this.Cena = Cena;
        this.DatumDolaska = DatumDolaska;
        this.DestiID = DestiID;
        this.SlobMesto = SlobMesto;
        this.KorisnikID = KorisnikID;
        this.RezerID = RezerID;
        this.DatumPolaska = DatumPolaska;
        this.PutnikID = PutnikID;
        this.kartas = new ArrayList<>();
    }

    public Rezervisanje(
        String Cena,        String DatumDolaska,        int DestiID,        boolean SlobMesto,        int KorisnikID,        int RezerID,        String DatumPolaska,        int PutnikID        ArrayList<Karta> kartas    ) {
        this.Cena = Cena;
        this.DatumDolaska = DatumDolaska;
        this.DestiID = DestiID;
        this.SlobMesto = SlobMesto;
        this.KorisnikID = KorisnikID;
        this.RezerID = RezerID;
        this.DatumPolaska = DatumPolaska;
        this.PutnikID = PutnikID;
        this.kartas = kartas;
    }

    public String getCena() {
        return Cena;
    }

    public void setCena(String Cena) {
        this.Cena = Cena;
    }
    public String getDatumdolaska() {
        return DatumDolaska;
    }

    public void setDatumdolaska(String DatumDolaska) {
        this.DatumDolaska = DatumDolaska;
    }
    public int getDestiid() {
        return DestiID;
    }

    public void setDestiid(int DestiID) {
        this.DestiID = DestiID;
    }
    public boolean getSlobmesto() {
        return SlobMesto;
    }

    public void setSlobmesto(boolean SlobMesto) {
        this.SlobMesto = SlobMesto;
    }
    public int getKorisnikid() {
        return KorisnikID;
    }

    public void setKorisnikid(int KorisnikID) {
        this.KorisnikID = KorisnikID;
    }
    public int getRezerid() {
        return RezerID;
    }

    public void setRezerid(int RezerID) {
        this.RezerID = RezerID;
    }
    public String getDatumpolaska() {
        return DatumPolaska;
    }

    public void setDatumpolaska(String DatumPolaska) {
        this.DatumPolaska = DatumPolaska;
    }
    public int getPutnikid() {
        return PutnikID;
    }

    public void setPutnikid(int PutnikID) {
        this.PutnikID = PutnikID;
    }

    public List<Karta> getKartas() {
        return kartas;
    }

    public void addKarta(Karta karta) {
        this.kartas.add(karta);
    }
    public Destinacija getDestinacija() {
        return destinacija;
    }

    public void setDestinacija(Destinacija destinacija) {
        this.destinacija = destinacija;
    }
    public Korisnik_IS getKorisnik_is() {
        return korisnik_is;
    }

    public void setKorisnik_is(Korisnik_IS korisnik_is) {
        this.korisnik_is = korisnik_is;
    }

}