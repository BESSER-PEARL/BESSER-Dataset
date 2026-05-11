





import java.util.List;
import java.util.ArrayList;

public class UML_14_Vererbung  {

    private String unterscheidung;





    private UML_14_Schachtel uml_14_schachtel;




    private List<UML_14_Konzept> uml_14_konzepts;




    private List<UML_14_Konzept> uml_14_konzepts;


    public UML_14_Vererbung(
        String unterscheidung    ) {
        this.unterscheidung = unterscheidung;
        this.uml_14_konzepts = new ArrayList<>();
        this.uml_14_konzepts = new ArrayList<>();
    }

    public UML_14_Vererbung(
        String unterscheidung        ArrayList<UML_14_Konzept> uml_14_konzepts,        ArrayList<UML_14_Konzept> uml_14_konzepts    ) {
        this.unterscheidung = unterscheidung;
        this.uml_14_konzepts = uml_14_konzepts;
        this.uml_14_konzepts = uml_14_konzepts;
    }

    public String getUnterscheidung() {
        return unterscheidung;
    }

    public void setUnterscheidung(String unterscheidung) {
        this.unterscheidung = unterscheidung;
    }

    public UML_14_Schachtel getUml_14_schachtel() {
        return uml_14_schachtel;
    }

    public void setUml_14_schachtel(UML_14_Schachtel uml_14_schachtel) {
        this.uml_14_schachtel = uml_14_schachtel;
    }
    public List<UML_14_Konzept> getUml_14_konzepts() {
        return uml_14_konzepts;
    }

    public void addUml_14_konzept(Uml_14_konzept uml_14_konzept) {
        this.uml_14_konzepts.add(uml_14_konzept);
    }
    public List<UML_14_Konzept> getUml_14_konzepts() {
        return uml_14_konzepts;
    }

    public void addUml_14_konzept(Uml_14_konzept uml_14_konzept) {
        this.uml_14_konzepts.add(uml_14_konzept);
    }

}