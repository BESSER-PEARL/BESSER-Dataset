





import java.util.List;
import java.util.ArrayList;

public class Entlehnung  {

    private String rueckGDatum;
    private int maxAnzahlFristTage;
    private String ausLeihFrist;
    private String ausLeihDatun;





    private List<Exemplar> exemplars;


    public Entlehnung(
        String rueckGDatum,        int maxAnzahlFristTage,        String ausLeihFrist,        String ausLeihDatun    ) {
        this.rueckGDatum = rueckGDatum;
        this.maxAnzahlFristTage = maxAnzahlFristTage;
        this.ausLeihFrist = ausLeihFrist;
        this.ausLeihDatun = ausLeihDatun;
        this.exemplars = new ArrayList<>();
    }

    public Entlehnung(
        String rueckGDatum,        int maxAnzahlFristTage,        String ausLeihFrist,        String ausLeihDatun        ArrayList<Exemplar> exemplars    ) {
        this.rueckGDatum = rueckGDatum;
        this.maxAnzahlFristTage = maxAnzahlFristTage;
        this.ausLeihFrist = ausLeihFrist;
        this.ausLeihDatun = ausLeihDatun;
        this.exemplars = exemplars;
    }

    public String getRueckgdatum() {
        return rueckGDatum;
    }

    public void setRueckgdatum(String rueckGDatum) {
        this.rueckGDatum = rueckGDatum;
    }
    public int getMaxanzahlfristtage() {
        return maxAnzahlFristTage;
    }

    public void setMaxanzahlfristtage(int maxAnzahlFristTage) {
        this.maxAnzahlFristTage = maxAnzahlFristTage;
    }
    public String getAusleihfrist() {
        return ausLeihFrist;
    }

    public void setAusleihfrist(String ausLeihFrist) {
        this.ausLeihFrist = ausLeihFrist;
    }
    public String getAusleihdatun() {
        return ausLeihDatun;
    }

    public void setAusleihdatun(String ausLeihDatun) {
        this.ausLeihDatun = ausLeihDatun;
    }

    public List<Exemplar> getExemplars() {
        return exemplars;
    }

    public void addExemplar(Exemplar exemplar) {
        this.exemplars.add(exemplar);
    }

}