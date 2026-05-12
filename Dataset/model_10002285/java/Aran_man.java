





import java.util.List;
import java.util.ArrayList;

public class Aran_man  {

    private String DatumDolaska;
    private int KorisnikID;
    private String Cena;
    private int PutovID;
    private boolean SlobMesto;
    private int KupacID;
    private int Aran_manID;
    private String DatumPolaska;





    private Korisnik_IS korisnik_is;




    private Putovanje putovanje;


    public Aran_man(
        String DatumDolaska,        int KorisnikID,        String Cena,        int PutovID,        boolean SlobMesto,        int KupacID,        int Aran_manID,        String DatumPolaska    ) {
        this.DatumDolaska = DatumDolaska;
        this.KorisnikID = KorisnikID;
        this.Cena = Cena;
        this.PutovID = PutovID;
        this.SlobMesto = SlobMesto;
        this.KupacID = KupacID;
        this.Aran_manID = Aran_manID;
        this.DatumPolaska = DatumPolaska;
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
    public String getCena() {
        return Cena;
    }

    public void setCena(String Cena) {
        this.Cena = Cena;
    }
    public int getPutovid() {
        return PutovID;
    }

    public void setPutovid(int PutovID) {
        this.PutovID = PutovID;
    }
    public boolean getSlobmesto() {
        return SlobMesto;
    }

    public void setSlobmesto(boolean SlobMesto) {
        this.SlobMesto = SlobMesto;
    }
    public int getKupacid() {
        return KupacID;
    }

    public void setKupacid(int KupacID) {
        this.KupacID = KupacID;
    }
    public int getAran_manid() {
        return Aran_manID;
    }

    public void setAran_manid(int Aran_manID) {
        this.Aran_manID = Aran_manID;
    }
    public String getDatumpolaska() {
        return DatumPolaska;
    }

    public void setDatumpolaska(String DatumPolaska) {
        this.DatumPolaska = DatumPolaska;
    }

    public Korisnik_IS getKorisnik_is() {
        return korisnik_is;
    }

    public void setKorisnik_is(Korisnik_IS korisnik_is) {
        this.korisnik_is = korisnik_is;
    }
    public Putovanje getPutovanje() {
        return putovanje;
    }

    public void setPutovanje(Putovanje putovanje) {
        this.putovanje = putovanje;
    }

}