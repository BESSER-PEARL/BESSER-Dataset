





import java.util.List;
import java.util.ArrayList;

public class zutaten  {

    private String zutatenListe;





    private plaetzchen plaetzchen;




    private zutat zutat;


    public zutaten(
        String zutatenListe    ) {
        this.zutatenListe = zutatenListe;
    }


    public String getZutatenliste() {
        return zutatenListe;
    }

    public void setZutatenliste(String zutatenListe) {
        this.zutatenListe = zutatenListe;
    }

    public plaetzchen getPlaetzchen() {
        return plaetzchen;
    }

    public void setPlaetzchen(plaetzchen plaetzchen) {
        this.plaetzchen = plaetzchen;
    }
    public zutat getZutat() {
        return zutat;
    }

    public void setZutat(zutat zutat) {
        this.zutat = zutat;
    }

}