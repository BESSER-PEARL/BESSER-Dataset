





import java.util.List;
import java.util.ArrayList;

public class UML_14_Verhalten extends Benanntes {

    private String inhlat;
    private String sichtbarkeit;





    private UML_14_MethodenWert uml_14_methodenwert;


    public UML_14_Verhalten(
        String inhlat,        String sichtbarkeit    ) {
        super(
        );
        this.inhlat = inhlat;
        this.sichtbarkeit = sichtbarkeit;
    }


    public String getInhlat() {
        return inhlat;
    }

    public void setInhlat(String inhlat) {
        this.inhlat = inhlat;
    }
    public String getSichtbarkeit() {
        return sichtbarkeit;
    }

    public void setSichtbarkeit(String sichtbarkeit) {
        this.sichtbarkeit = sichtbarkeit;
    }

    public UML_14_MethodenWert getUml_14_methodenwert() {
        return uml_14_methodenwert;
    }

    public void setUml_14_methodenwert(UML_14_MethodenWert uml_14_methodenwert) {
        this.uml_14_methodenwert = uml_14_methodenwert;
    }

}