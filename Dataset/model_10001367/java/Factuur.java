





import java.util.List;
import java.util.ArrayList;

public class Factuur  {

    private int btw;
    private String status;
    private String datum;





    private Klant klant;




    private Beheerder beheerder;


    public Factuur(
        int btw,        String status,        String datum    ) {
        this.btw = btw;
        this.status = status;
        this.datum = datum;
    }


    public int getBtw() {
        return btw;
    }

    public void setBtw(int btw) {
        this.btw = btw;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getDatum() {
        return datum;
    }

    public void setDatum(String datum) {
        this.datum = datum;
    }

    public Klant getKlant() {
        return klant;
    }

    public void setKlant(Klant klant) {
        this.klant = klant;
    }
    public Beheerder getBeheerder() {
        return beheerder;
    }

    public void setBeheerder(Beheerder beheerder) {
        this.beheerder = beheerder;
    }

}