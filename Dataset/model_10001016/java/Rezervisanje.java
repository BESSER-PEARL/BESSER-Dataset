





import java.util.List;
import java.util.ArrayList;

public class Rezervisanje  {

    private int DestiID;
    private String DatumDolaska;
    private int KorisnikID;
    private boolean SlobMesto;
    private String DatumPolaska;
    private int RezerID;
    private int PutnikID;
    private String Cena;





    private Destinacija destinacija;




    private List<Karta> kartas;


    public Rezervisanje(
        int DestiID,        String DatumDolaska,        int KorisnikID,        boolean SlobMesto,        String DatumPolaska,        int RezerID,        int PutnikID,        String Cena    ) {
        this.DestiID = DestiID;
        this.DatumDolaska = DatumDolaska;
        this.KorisnikID = KorisnikID;
        this.SlobMesto = SlobMesto;
        this.DatumPolaska = DatumPolaska;
        this.RezerID = RezerID;
        this.PutnikID = PutnikID;
        this.Cena = Cena;
        this.kartas = new ArrayList<>();
    }

    public Rezervisanje(
        int DestiID,        String DatumDolaska,        int KorisnikID,        boolean SlobMesto,        String DatumPolaska,        int RezerID,        int PutnikID,        String Cena        ArrayList<Karta> kartas    ) {
        this.DestiID = DestiID;
        this.DatumDolaska = DatumDolaska;
        this.KorisnikID = KorisnikID;
        this.SlobMesto = SlobMesto;
        this.DatumPolaska = DatumPolaska;
        this.RezerID = RezerID;
        this.PutnikID = PutnikID;
        this.Cena = Cena;
        this.kartas = kartas;
    }

    public int getDestiid() {
        return DestiID;
    }

    public void setDestiid(int DestiID) {
        this.DestiID = DestiID;
    }
    public String getDatumdolaska() {
        return DatumDolaska;
    }

    public void setDatumdolaska(String DatumDolaska) {
        this.DatumDolaska = DatumDolaska;
    }
    public int getKorisnikid() {
        return KorisnikID;
    }

    public void setKorisnikid(int KorisnikID) {
        this.KorisnikID = KorisnikID;
    }
    public boolean getSlobmesto() {
        return SlobMesto;
    }

    public void setSlobmesto(boolean SlobMesto) {
        this.SlobMesto = SlobMesto;
    }
    public String getDatumpolaska() {
        return DatumPolaska;
    }

    public void setDatumpolaska(String DatumPolaska) {
        this.DatumPolaska = DatumPolaska;
    }
    public int getRezerid() {
        return RezerID;
    }

    public void setRezerid(int RezerID) {
        this.RezerID = RezerID;
    }
    public int getPutnikid() {
        return PutnikID;
    }

    public void setPutnikid(int PutnikID) {
        this.PutnikID = PutnikID;
    }
    public String getCena() {
        return Cena;
    }

    public void setCena(String Cena) {
        this.Cena = Cena;
    }

    public Destinacija getDestinacija() {
        return destinacija;
    }

    public void setDestinacija(Destinacija destinacija) {
        this.destinacija = destinacija;
    }
    public List<Karta> getKartas() {
        return kartas;
    }

    public void addKarta(Karta karta) {
        this.kartas.add(karta);
    }

}