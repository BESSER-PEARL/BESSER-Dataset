





import java.util.List;
import java.util.ArrayList;

public class uml_RedefinableTemplateSignature extends TemplateSignature, RedefinableElement {






    private List<uml_RedefinableTemplateSignature> uml_redefinabletemplatesignatures;




    private uml_Classifier uml_classifier;




    private List<uml_TemplateParameter> uml_templateparameters;


    public uml_RedefinableTemplateSignature(
    ) {
        super(
        );
        this.uml_redefinabletemplatesignatures = new ArrayList<>();
        this.uml_templateparameters = new ArrayList<>();
    }

    public uml_RedefinableTemplateSignature(
        ArrayList<uml_RedefinableTemplateSignature> uml_redefinabletemplatesignatures,        ArrayList<uml_TemplateParameter> uml_templateparameters    ) {
        this.uml_redefinabletemplatesignatures = uml_redefinabletemplatesignatures;
        this.uml_templateparameters = uml_templateparameters;
    }


    public List<uml_RedefinableTemplateSignature> getUml_redefinabletemplatesignatures() {
        return uml_redefinabletemplatesignatures;
    }

    public void addUml_redefinabletemplatesignature(Uml_redefinabletemplatesignature uml_redefinabletemplatesignature) {
        this.uml_redefinabletemplatesignatures.add(uml_redefinabletemplatesignature);
    }
    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }
    public List<uml_TemplateParameter> getUml_templateparameters() {
        return uml_templateparameters;
    }

    public void addUml_templateparameter(Uml_templateparameter uml_templateparameter) {
        this.uml_templateparameters.add(uml_templateparameter);
    }

}