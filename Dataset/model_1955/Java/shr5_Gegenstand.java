





import java.util.List;
import java.util.ArrayList;

public class shr5_Gegenstand extends AbstraktGegenstand {

    private String kategorie;
    private int stufe;



    public shr5_Gegenstand(
        String kategorie,        int stufe    ) {
        super(
        );
        this.kategorie = kategorie;
        this.stufe = stufe;
    }


    public String getKategorie() {
        return kategorie;
    }

    public void setKategorie(String kategorie) {
        this.kategorie = kategorie;
    }
    public int getStufe() {
        return stufe;
    }

    public void setStufe(int stufe) {
        this.stufe = stufe;
    }


}