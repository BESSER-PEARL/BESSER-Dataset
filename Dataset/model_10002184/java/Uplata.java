





import java.util.List;
import java.util.ArrayList;

public class Uplata  {

    private String DatumUplate;
    private String NazivUplate;
    private int PutnikID;
    private int UplataID;
    private String Iznos;





    private Putnik putnik;


    public Uplata(
        String DatumUplate,        String NazivUplate,        int PutnikID,        int UplataID,        String Iznos    ) {
        this.DatumUplate = DatumUplate;
        this.NazivUplate = NazivUplate;
        this.PutnikID = PutnikID;
        this.UplataID = UplataID;
        this.Iznos = Iznos;
    }


    public String getDatumuplate() {
        return DatumUplate;
    }

    public void setDatumuplate(String DatumUplate) {
        this.DatumUplate = DatumUplate;
    }
    public String getNazivuplate() {
        return NazivUplate;
    }

    public void setNazivuplate(String NazivUplate) {
        this.NazivUplate = NazivUplate;
    }
    public int getPutnikid() {
        return PutnikID;
    }

    public void setPutnikid(int PutnikID) {
        this.PutnikID = PutnikID;
    }
    public int getUplataid() {
        return UplataID;
    }

    public void setUplataid(int UplataID) {
        this.UplataID = UplataID;
    }
    public String getIznos() {
        return Iznos;
    }

    public void setIznos(String Iznos) {
        this.Iznos = Iznos;
    }

    public Putnik getPutnik() {
        return putnik;
    }

    public void setPutnik(Putnik putnik) {
        this.putnik = putnik;
    }

}