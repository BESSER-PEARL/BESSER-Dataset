





import java.util.List;
import java.util.ArrayList;

public class UML_14_Verbindungsende extends Benanntes {

    private String istNavigierbar;
    private String sichtbarkeit;





    private UML_14_Verbindung uml_14_verbindung;




    private UML_14_Eigenschaft uml_14_eigenschaft;




    private UML_14_Konzept uml_14_konzept;




    private UML_14_Verbindung uml_14_verbindung;


    public UML_14_Verbindungsende(
        String istNavigierbar,        String sichtbarkeit    ) {
        super(
        );
        this.istNavigierbar = istNavigierbar;
        this.sichtbarkeit = sichtbarkeit;
    }


    public String getIstnavigierbar() {
        return istNavigierbar;
    }

    public void setIstnavigierbar(String istNavigierbar) {
        this.istNavigierbar = istNavigierbar;
    }
    public String getSichtbarkeit() {
        return sichtbarkeit;
    }

    public void setSichtbarkeit(String sichtbarkeit) {
        this.sichtbarkeit = sichtbarkeit;
    }

    public UML_14_Verbindung getUml_14_verbindung() {
        return uml_14_verbindung;
    }

    public void setUml_14_verbindung(UML_14_Verbindung uml_14_verbindung) {
        this.uml_14_verbindung = uml_14_verbindung;
    }
    public UML_14_Eigenschaft getUml_14_eigenschaft() {
        return uml_14_eigenschaft;
    }

    public void setUml_14_eigenschaft(UML_14_Eigenschaft uml_14_eigenschaft) {
        this.uml_14_eigenschaft = uml_14_eigenschaft;
    }
    public UML_14_Konzept getUml_14_konzept() {
        return uml_14_konzept;
    }

    public void setUml_14_konzept(UML_14_Konzept uml_14_konzept) {
        this.uml_14_konzept = uml_14_konzept;
    }
    public UML_14_Verbindung getUml_14_verbindung() {
        return uml_14_verbindung;
    }

    public void setUml_14_verbindung(UML_14_Verbindung uml_14_verbindung) {
        this.uml_14_verbindung = uml_14_verbindung;
    }

}