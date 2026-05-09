





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_RedefinableTemplateSignature extends TemplateSignature, RedefinableElement {






    private List<uml3_0_0_TemplateParameter> uml3_0_0_templateparameters;




    private uml3_0_0_RedefinableTemplateSignature uml3_0_0_redefinabletemplatesignature;




    private uml3_0_0_Classifier uml3_0_0_classifier;


    public uml3_0_0_RedefinableTemplateSignature(
    ) {
        super(
        );
        this.uml3_0_0_templateparameters = new ArrayList<>();
    }

    public uml3_0_0_RedefinableTemplateSignature(
        ArrayList<uml3_0_0_TemplateParameter> uml3_0_0_templateparameters    ) {
        this.uml3_0_0_templateparameters = uml3_0_0_templateparameters;
    }


    public List<uml3_0_0_TemplateParameter> getUml3_0_0_templateparameters() {
        return uml3_0_0_templateparameters;
    }

    public void addUml3_0_0_templateparameter(Uml3_0_0_templateparameter uml3_0_0_templateparameter) {
        this.uml3_0_0_templateparameters.add(uml3_0_0_templateparameter);
    }
    public uml3_0_0_RedefinableTemplateSignature getUml3_0_0_redefinabletemplatesignature() {
        return uml3_0_0_redefinabletemplatesignature;
    }

    public void setUml3_0_0_redefinabletemplatesignature(uml3_0_0_RedefinableTemplateSignature uml3_0_0_redefinabletemplatesignature) {
        this.uml3_0_0_redefinabletemplatesignature = uml3_0_0_redefinabletemplatesignature;
    }
    public uml3_0_0_Classifier getUml3_0_0_classifier() {
        return uml3_0_0_classifier;
    }

    public void setUml3_0_0_classifier(uml3_0_0_Classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifier = uml3_0_0_classifier;
    }

}