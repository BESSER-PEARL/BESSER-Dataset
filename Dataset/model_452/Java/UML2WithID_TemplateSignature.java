





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_TemplateSignature extends Element {






    private UML2WithID_TemplateableElement uml2withid_templateableelement;




    private List<UML2WithID_TemplateParameter> uml2withid_templateparameters;




    private List<UML2WithID_TemplateSignature> uml2withid_templatesignatures;




    private UML2WithID_TemplateSignature uml2withid_templatesignature;




    private UML2WithID_TemplateParameter uml2withid_templateparameter;




    private UML2WithID_TemplateableElement uml2withid_templateableelement;




    private List<UML2WithID_TemplateParameter> uml2withid_templateparameters;




    private UML2WithID_TemplateBinding uml2withid_templatebinding;


    public UML2WithID_TemplateSignature(
    ) {
        super(
        );
        this.uml2withid_templateparameters = new ArrayList<>();
        this.uml2withid_templatesignatures = new ArrayList<>();
        this.uml2withid_templateparameters = new ArrayList<>();
    }

    public UML2WithID_TemplateSignature(
        ArrayList<UML2WithID_TemplateParameter> uml2withid_templateparameters,        ArrayList<UML2WithID_TemplateSignature> uml2withid_templatesignatures,        ArrayList<UML2WithID_TemplateParameter> uml2withid_templateparameters    ) {
        this.uml2withid_templateparameters = uml2withid_templateparameters;
        this.uml2withid_templatesignatures = uml2withid_templatesignatures;
        this.uml2withid_templateparameters = uml2withid_templateparameters;
    }


    public UML2WithID_TemplateableElement getUml2withid_templateableelement() {
        return uml2withid_templateableelement;
    }

    public void setUml2withid_templateableelement(UML2WithID_TemplateableElement uml2withid_templateableelement) {
        this.uml2withid_templateableelement = uml2withid_templateableelement;
    }
    public List<UML2WithID_TemplateParameter> getUml2withid_templateparameters() {
        return uml2withid_templateparameters;
    }

    public void addUml2withid_templateparameter(Uml2withid_templateparameter uml2withid_templateparameter) {
        this.uml2withid_templateparameters.add(uml2withid_templateparameter);
    }
    public List<UML2WithID_TemplateSignature> getUml2withid_templatesignatures() {
        return uml2withid_templatesignatures;
    }

    public void addUml2withid_templatesignature(Uml2withid_templatesignature uml2withid_templatesignature) {
        this.uml2withid_templatesignatures.add(uml2withid_templatesignature);
    }
    public UML2WithID_TemplateSignature getUml2withid_templatesignature() {
        return uml2withid_templatesignature;
    }

    public void setUml2withid_templatesignature(UML2WithID_TemplateSignature uml2withid_templatesignature) {
        this.uml2withid_templatesignature = uml2withid_templatesignature;
    }
    public UML2WithID_TemplateParameter getUml2withid_templateparameter() {
        return uml2withid_templateparameter;
    }

    public void setUml2withid_templateparameter(UML2WithID_TemplateParameter uml2withid_templateparameter) {
        this.uml2withid_templateparameter = uml2withid_templateparameter;
    }
    public UML2WithID_TemplateableElement getUml2withid_templateableelement() {
        return uml2withid_templateableelement;
    }

    public void setUml2withid_templateableelement(UML2WithID_TemplateableElement uml2withid_templateableelement) {
        this.uml2withid_templateableelement = uml2withid_templateableelement;
    }
    public List<UML2WithID_TemplateParameter> getUml2withid_templateparameters() {
        return uml2withid_templateparameters;
    }

    public void addUml2withid_templateparameter(Uml2withid_templateparameter uml2withid_templateparameter) {
        this.uml2withid_templateparameters.add(uml2withid_templateparameter);
    }
    public UML2WithID_TemplateBinding getUml2withid_templatebinding() {
        return uml2withid_templatebinding;
    }

    public void setUml2withid_templatebinding(UML2WithID_TemplateBinding uml2withid_templatebinding) {
        this.uml2withid_templatebinding = uml2withid_templatebinding;
    }

}