





import java.util.List;
import java.util.ArrayList;

public class UML_14_InstanzAnzahl  {

    private String untergrenze;
    private String obergrenze;





    private UML_14_Verbindungsende uml_14_verbindungsende;




    private UML_14_Eigenschaft uml_14_eigenschaft;


    public UML_14_InstanzAnzahl(
        String untergrenze,        String obergrenze    ) {
        this.untergrenze = untergrenze;
        this.obergrenze = obergrenze;
    }


    public String getUntergrenze() {
        return untergrenze;
    }

    public void setUntergrenze(String untergrenze) {
        this.untergrenze = untergrenze;
    }
    public String getObergrenze() {
        return obergrenze;
    }

    public void setObergrenze(String obergrenze) {
        this.obergrenze = obergrenze;
    }

    public UML_14_Verbindungsende getUml_14_verbindungsende() {
        return uml_14_verbindungsende;
    }

    public void setUml_14_verbindungsende(UML_14_Verbindungsende uml_14_verbindungsende) {
        this.uml_14_verbindungsende = uml_14_verbindungsende;
    }
    public UML_14_Eigenschaft getUml_14_eigenschaft() {
        return uml_14_eigenschaft;
    }

    public void setUml_14_eigenschaft(UML_14_Eigenschaft uml_14_eigenschaft) {
        this.uml_14_eigenschaft = uml_14_eigenschaft;
    }

}