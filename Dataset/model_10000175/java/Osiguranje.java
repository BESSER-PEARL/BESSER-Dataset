





import java.util.List;
import java.util.ArrayList;

public class Osiguranje  {

    private String Osiguranje_ID;
    private String PaketPokri_a;
    private int BrojPolise;
    private String Cena;
    private String OsigKuca;



    public Osiguranje(
        String Osiguranje_ID,        String PaketPokri_a,        int BrojPolise,        String Cena,        String OsigKuca    ) {
        this.Osiguranje_ID = Osiguranje_ID;
        this.PaketPokri_a = PaketPokri_a;
        this.BrojPolise = BrojPolise;
        this.Cena = Cena;
        this.OsigKuca = OsigKuca;
    }


    public String getOsiguranje_id() {
        return Osiguranje_ID;
    }

    public void setOsiguranje_id(String Osiguranje_ID) {
        this.Osiguranje_ID = Osiguranje_ID;
    }
    public String getPaketpokri_a() {
        return PaketPokri_a;
    }

    public void setPaketpokri_a(String PaketPokri_a) {
        this.PaketPokri_a = PaketPokri_a;
    }
    public int getBrojpolise() {
        return BrojPolise;
    }

    public void setBrojpolise(int BrojPolise) {
        this.BrojPolise = BrojPolise;
    }
    public String getCena() {
        return Cena;
    }

    public void setCena(String Cena) {
        this.Cena = Cena;
    }
    public String getOsigkuca() {
        return OsigKuca;
    }

    public void setOsigkuca(String OsigKuca) {
        this.OsigKuca = OsigKuca;
    }


}