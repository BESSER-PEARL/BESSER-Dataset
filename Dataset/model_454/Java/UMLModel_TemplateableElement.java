





import java.util.List;
import java.util.ArrayList;

public class UMLModel_TemplateableElement extends Element {






    private List<UMLModel_TemplateBinding> umlmodel_templatebindings;




    private UMLModel_TemplateSignature umlmodel_templatesignature;


    public UMLModel_TemplateableElement(
    ) {
        super(
        );
        this.umlmodel_templatebindings = new ArrayList<>();
    }

    public UMLModel_TemplateableElement(
        ArrayList<UMLModel_TemplateBinding> umlmodel_templatebindings    ) {
        this.umlmodel_templatebindings = umlmodel_templatebindings;
    }


    public List<UMLModel_TemplateBinding> getUmlmodel_templatebindings() {
        return umlmodel_templatebindings;
    }

    public void addUmlmodel_templatebinding(Umlmodel_templatebinding umlmodel_templatebinding) {
        this.umlmodel_templatebindings.add(umlmodel_templatebinding);
    }
    public UMLModel_TemplateSignature getUmlmodel_templatesignature() {
        return umlmodel_templatesignature;
    }

    public void setUmlmodel_templatesignature(UMLModel_TemplateSignature umlmodel_templatesignature) {
        this.umlmodel_templatesignature = umlmodel_templatesignature;
    }

}