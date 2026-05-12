





import java.util.List;
import java.util.ArrayList;

public class Osiguranje  {

    private String PaketPokri_a;
    private int OsigID;
    private String KucaOsiguranje;



    public Osiguranje(
        String PaketPokri_a,        int OsigID,        String KucaOsiguranje    ) {
        this.PaketPokri_a = PaketPokri_a;
        this.OsigID = OsigID;
        this.KucaOsiguranje = KucaOsiguranje;
    }


    public String getPaketpokri_a() {
        return PaketPokri_a;
    }

    public void setPaketpokri_a(String PaketPokri_a) {
        this.PaketPokri_a = PaketPokri_a;
    }
    public int getOsigid() {
        return OsigID;
    }

    public void setOsigid(int OsigID) {
        this.OsigID = OsigID;
    }
    public String getKucaosiguranje() {
        return KucaOsiguranje;
    }

    public void setKucaosiguranje(String KucaOsiguranje) {
        this.KucaOsiguranje = KucaOsiguranje;
    }


}