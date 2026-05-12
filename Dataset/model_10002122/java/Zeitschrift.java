





import java.util.List;
import java.util.ArrayList;

public class Zeitschrift  {

    private String Ausgabe;
    private int Jahrgang;



    public Zeitschrift(
        String Ausgabe,        int Jahrgang    ) {
        this.Ausgabe = Ausgabe;
        this.Jahrgang = Jahrgang;
    }


    public String getAusgabe() {
        return Ausgabe;
    }

    public void setAusgabe(String Ausgabe) {
        this.Ausgabe = Ausgabe;
    }
    public int getJahrgang() {
        return Jahrgang;
    }

    public void setJahrgang(int Jahrgang) {
        this.Jahrgang = Jahrgang;
    }


}