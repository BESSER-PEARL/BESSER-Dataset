





import java.util.List;
import java.util.ArrayList;

public class aadl2_AnnexSubclause extends ModalElement {






    private aadl2_Classifier aadl2_classifier;




    private aadl2_PropertySet aadl2_propertyset;




    private aadl2_DefaultAnnexSubclause aadl2_defaultannexsubclause;


    public aadl2_AnnexSubclause(
    ) {
        super(
        );
    }



    public aadl2_Classifier getAadl2_classifier() {
        return aadl2_classifier;
    }

    public void setAadl2_classifier(aadl2_Classifier aadl2_classifier) {
        this.aadl2_classifier = aadl2_classifier;
    }
    public aadl2_PropertySet getAadl2_propertyset() {
        return aadl2_propertyset;
    }

    public void setAadl2_propertyset(aadl2_PropertySet aadl2_propertyset) {
        this.aadl2_propertyset = aadl2_propertyset;
    }
    public aadl2_DefaultAnnexSubclause getAadl2_defaultannexsubclause() {
        return aadl2_defaultannexsubclause;
    }

    public void setAadl2_defaultannexsubclause(aadl2_DefaultAnnexSubclause aadl2_defaultannexsubclause) {
        this.aadl2_defaultannexsubclause = aadl2_defaultannexsubclause;
    }

}