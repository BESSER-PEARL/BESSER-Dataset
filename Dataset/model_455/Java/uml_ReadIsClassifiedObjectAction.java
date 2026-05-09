





import java.util.List;
import java.util.ArrayList;

public class uml_ReadIsClassifiedObjectAction extends Action {

    private String isDirect;





    private uml_Classifier uml_classifier;


    public uml_ReadIsClassifiedObjectAction(
        String isDirect    ) {
        super(
        );
        this.isDirect = isDirect;
    }


    public String getIsdirect() {
        return isDirect;
    }

    public void setIsdirect(String isDirect) {
        this.isDirect = isDirect;
    }

    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }

}