





import java.util.List;
import java.util.ArrayList;

public class Rezervisanje  {

    private int PutnikID;
    private int RezerID;
    private String DatumPolaska;
    private int KorisnikID;
    private String Cena;
    private String DatumDolaska;
    private int DestiID;
    private boolean SlobMesto;





    private List<Karta> kartas;




    private Destinacija destinacija;


    public Rezervisanje(
        int PutnikID,        int RezerID,        String DatumPolaska,        int KorisnikID,        String Cena,        String DatumDolaska,        int DestiID,        boolean SlobMesto    ) {
        this.PutnikID = PutnikID;
        this.RezerID = RezerID;
        this.DatumPolaska = DatumPolaska;
        this.KorisnikID = KorisnikID;
        this.Cena = Cena;
        this.DatumDolaska = DatumDolaska;
        this.DestiID = DestiID;
        this.SlobMesto = SlobMesto;
        this.kartas = new ArrayList<>();
    }

    public Rezervisanje(
        int PutnikID,        int RezerID,        String DatumPolaska,        int KorisnikID,        String Cena,        String DatumDolaska,        int DestiID,        boolean SlobMesto        ArrayList<Karta> kartas    ) {
        this.PutnikID = PutnikID;
        this.RezerID = RezerID;
        this.DatumPolaska = DatumPolaska;
        this.KorisnikID = KorisnikID;
        this.Cena = Cena;
        this.DatumDolaska = DatumDolaska;
        this.DestiID = DestiID;
        this.SlobMesto = SlobMesto;
        this.kartas = kartas;
    }

    public int getPutnikid() {
        return PutnikID;
    }

    public void setPutnikid(int PutnikID) {
        this.PutnikID = PutnikID;
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
    public int getKorisnikid() {
        return KorisnikID;
    }

    public void setKorisnikid(int KorisnikID) {
        this.KorisnikID = KorisnikID;
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

}