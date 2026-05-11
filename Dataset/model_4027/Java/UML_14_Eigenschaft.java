





import java.util.List;
import java.util.ArrayList;

public class UML_14_Eigenschaft extends Benanntes {

    private String initialWert;
    private String sichtbarkeit;



    public UML_14_Eigenschaft(
        String initialWert,        String sichtbarkeit    ) {
        super(
        );
        this.initialWert = initialWert;
        this.sichtbarkeit = sichtbarkeit;
    }


    public String getInitialwert() {
        return initialWert;
    }

    public void setInitialwert(String initialWert) {
        this.initialWert = initialWert;
    }
    public String getSichtbarkeit() {
        return sichtbarkeit;
    }

    public void setSichtbarkeit(String sichtbarkeit) {
        this.sichtbarkeit = sichtbarkeit;
    }


}