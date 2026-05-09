





import java.util.List;
import java.util.ArrayList;

public class UML2_TemplateSignature extends Element {






    private UML2_TemplateSignature uml2_templatesignature;




    private List<UML2_TemplateParameter> uml2_templateparameters;




    private UML2_TemplateSignature uml2_templatesignature;




    private UML2_TemplateableElement uml2_templateableelement;




    private UML2_TemplateParameter uml2_templateparameter;




    private UML2_TemplateableElement uml2_templateableelement;




    private List<UML2_TemplateParameter> uml2_templateparameters;


    public UML2_TemplateSignature(
    ) {
        super(
        );
        this.uml2_templateparameters = new ArrayList<>();
        this.uml2_templateparameters = new ArrayList<>();
    }

    public UML2_TemplateSignature(
        ArrayList<UML2_TemplateParameter> uml2_templateparameters,        ArrayList<UML2_TemplateParameter> uml2_templateparameters    ) {
        this.uml2_templateparameters = uml2_templateparameters;
        this.uml2_templateparameters = uml2_templateparameters;
    }


    public UML2_TemplateSignature getUml2_templatesignature() {
        return uml2_templatesignature;
    }

    public void setUml2_templatesignature(UML2_TemplateSignature uml2_templatesignature) {
        this.uml2_templatesignature = uml2_templatesignature;
    }
    public List<UML2_TemplateParameter> getUml2_templateparameters() {
        return uml2_templateparameters;
    }

    public void addUml2_templateparameter(Uml2_templateparameter uml2_templateparameter) {
        this.uml2_templateparameters.add(uml2_templateparameter);
    }
    public UML2_TemplateSignature getUml2_templatesignature() {
        return uml2_templatesignature;
    }

    public void setUml2_templatesignature(UML2_TemplateSignature uml2_templatesignature) {
        this.uml2_templatesignature = uml2_templatesignature;
    }
    public UML2_TemplateableElement getUml2_templateableelement() {
        return uml2_templateableelement;
    }

    public void setUml2_templateableelement(UML2_TemplateableElement uml2_templateableelement) {
        this.uml2_templateableelement = uml2_templateableelement;
    }
    public UML2_TemplateParameter getUml2_templateparameter() {
        return uml2_templateparameter;
    }

    public void setUml2_templateparameter(UML2_TemplateParameter uml2_templateparameter) {
        this.uml2_templateparameter = uml2_templateparameter;
    }
    public UML2_TemplateableElement getUml2_templateableelement() {
        return uml2_templateableelement;
    }

    public void setUml2_templateableelement(UML2_TemplateableElement uml2_templateableelement) {
        this.uml2_templateableelement = uml2_templateableelement;
    }
    public List<UML2_TemplateParameter> getUml2_templateparameters() {
        return uml2_templateparameters;
    }

    public void addUml2_templateparameter(Uml2_templateparameter uml2_templateparameter) {
        this.uml2_templateparameters.add(uml2_templateparameter);
    }

}