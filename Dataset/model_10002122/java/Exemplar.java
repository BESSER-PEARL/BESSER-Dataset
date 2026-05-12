





import java.util.List;
import java.util.ArrayList;

public class Exemplar  {

    private String exemplarNummer;





    private Entleihungsgegenstand entleihungsgegenstand;


    public Exemplar(
        String exemplarNummer    ) {
        this.exemplarNummer = exemplarNummer;
    }


    public String getExemplarnummer() {
        return exemplarNummer;
    }

    public void setExemplarnummer(String exemplarNummer) {
        this.exemplarNummer = exemplarNummer;
    }

    public Entleihungsgegenstand getEntleihungsgegenstand() {
        return entleihungsgegenstand;
    }

    public void setEntleihungsgegenstand(Entleihungsgegenstand entleihungsgegenstand) {
        this.entleihungsgegenstand = entleihungsgegenstand;
    }

}