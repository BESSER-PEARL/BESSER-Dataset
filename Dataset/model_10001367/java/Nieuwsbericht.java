





import java.util.List;
import java.util.ArrayList;

public class Nieuwsbericht  {

    private String tekst;
    private String titel;





    private Hoofdbeheerder hoofdbeheerder;


    public Nieuwsbericht(
        String tekst,        String titel    ) {
        this.tekst = tekst;
        this.titel = titel;
    }


    public String getTekst() {
        return tekst;
    }

    public void setTekst(String tekst) {
        this.tekst = tekst;
    }
    public String getTitel() {
        return titel;
    }

    public void setTitel(String titel) {
        this.titel = titel;
    }

    public Hoofdbeheerder getHoofdbeheerder() {
        return hoofdbeheerder;
    }

    public void setHoofdbeheerder(Hoofdbeheerder hoofdbeheerder) {
        this.hoofdbeheerder = hoofdbeheerder;
    }

}