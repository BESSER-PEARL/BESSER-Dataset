





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ParameterableElement extends Element {

    private String owningTemplateParameter;
    private String templateParameter;





    private UMLModel_TemplateParameter umlmodel_templateparameter;




    private UMLModel_TemplateParameter umlmodel_templateparameter;


    public UMLModel_ParameterableElement(
        String owningTemplateParameter,        String templateParameter    ) {
        super(
        );
        this.owningTemplateParameter = owningTemplateParameter;
        this.templateParameter = templateParameter;
    }


    public String getOwningtemplateparameter() {
        return owningTemplateParameter;
    }

    public void setOwningtemplateparameter(String owningTemplateParameter) {
        this.owningTemplateParameter = owningTemplateParameter;
    }
    public String getTemplateparameter() {
        return templateParameter;
    }

    public void setTemplateparameter(String templateParameter) {
        this.templateParameter = templateParameter;
    }

    public UMLModel_TemplateParameter getUmlmodel_templateparameter() {
        return umlmodel_templateparameter;
    }

    public void setUmlmodel_templateparameter(UMLModel_TemplateParameter umlmodel_templateparameter) {
        this.umlmodel_templateparameter = umlmodel_templateparameter;
    }
    public UMLModel_TemplateParameter getUmlmodel_templateparameter() {
        return umlmodel_templateparameter;
    }

    public void setUmlmodel_templateparameter(UMLModel_TemplateParameter umlmodel_templateparameter) {
        this.umlmodel_templateparameter = umlmodel_templateparameter;
    }

}