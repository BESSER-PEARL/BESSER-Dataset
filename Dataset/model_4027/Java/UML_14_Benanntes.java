





import java.util.List;
import java.util.ArrayList;

public class UML_14_Benanntes  {

    private String beschreibung;





    private List<UML_14_Kommentar> uml_14_kommentars;




    private List<UML_14_Einschraenkung> uml_14_einschraenkungs;


    public UML_14_Benanntes(
        String beschreibung    ) {
        this.beschreibung = beschreibung;
        this.uml_14_kommentars = new ArrayList<>();
        this.uml_14_einschraenkungs = new ArrayList<>();
    }

    public UML_14_Benanntes(
        String beschreibung        ArrayList<UML_14_Kommentar> uml_14_kommentars,        ArrayList<UML_14_Einschraenkung> uml_14_einschraenkungs    ) {
        this.beschreibung = beschreibung;
        this.uml_14_kommentars = uml_14_kommentars;
        this.uml_14_einschraenkungs = uml_14_einschraenkungs;
    }

    public String getBeschreibung() {
        return beschreibung;
    }

    public void setBeschreibung(String beschreibung) {
        this.beschreibung = beschreibung;
    }

    public List<UML_14_Kommentar> getUml_14_kommentars() {
        return uml_14_kommentars;
    }

    public void addUml_14_kommentar(Uml_14_kommentar uml_14_kommentar) {
        this.uml_14_kommentars.add(uml_14_kommentar);
    }
    public List<UML_14_Einschraenkung> getUml_14_einschraenkungs() {
        return uml_14_einschraenkungs;
    }

    public void addUml_14_einschraenkung(Uml_14_einschraenkung uml_14_einschraenkung) {
        this.uml_14_einschraenkungs.add(uml_14_einschraenkung);
    }

}