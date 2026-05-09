





import java.util.List;
import java.util.ArrayList;

public class UMLModel_TemplateParameter extends Element {

    private String signature;
    private String parameteredElement;
    private String default;





    private UMLModel_TemplateSignature umlmodel_templatesignature;


    public UMLModel_TemplateParameter(
        String signature,        String parameteredElement,        String default    ) {
        super(
        );
        this.signature = signature;
        this.parameteredElement = parameteredElement;
        this.default = default;
    }


    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }
    public String getParameteredelement() {
        return parameteredElement;
    }

    public void setParameteredelement(String parameteredElement) {
        this.parameteredElement = parameteredElement;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public UMLModel_TemplateSignature getUmlmodel_templatesignature() {
        return umlmodel_templatesignature;
    }

    public void setUmlmodel_templatesignature(UMLModel_TemplateSignature umlmodel_templatesignature) {
        this.umlmodel_templatesignature = umlmodel_templatesignature;
    }

}