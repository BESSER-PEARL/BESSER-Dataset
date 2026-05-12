





import java.util.List;
import java.util.ArrayList;

public class Osiguranje  {

    private int OsigID;
    private String KucaOsiguranje;



    public Osiguranje(
        int OsigID,        String KucaOsiguranje    ) {
        this.OsigID = OsigID;
        this.KucaOsiguranje = KucaOsiguranje;
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