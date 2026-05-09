





import java.util.List;
import java.util.ArrayList;

public class UMLModel_TemplateParameterSubstitution extends Element {

    private String formal;
    private String actual;
    private String templateBinding;





    private UMLModel_TemplateBinding umlmodel_templatebinding;




    private List<UMLModel_ParameterableElement> umlmodel_parameterableelements;


    public UMLModel_TemplateParameterSubstitution(
        String formal,        String actual,        String templateBinding    ) {
        super(
        );
        this.formal = formal;
        this.actual = actual;
        this.templateBinding = templateBinding;
        this.umlmodel_parameterableelements = new ArrayList<>();
    }

    public UMLModel_TemplateParameterSubstitution(
        String formal,        String actual,        String templateBinding        ArrayList<UMLModel_ParameterableElement> umlmodel_parameterableelements    ) {
        this.formal = formal;
        this.actual = actual;
        this.templateBinding = templateBinding;
        this.umlmodel_parameterableelements = umlmodel_parameterableelements;
    }

    public String getFormal() {
        return formal;
    }

    public void setFormal(String formal) {
        this.formal = formal;
    }
    public String getActual() {
        return actual;
    }

    public void setActual(String actual) {
        this.actual = actual;
    }
    public String getTemplatebinding() {
        return templateBinding;
    }

    public void setTemplatebinding(String templateBinding) {
        this.templateBinding = templateBinding;
    }

    public UMLModel_TemplateBinding getUmlmodel_templatebinding() {
        return umlmodel_templatebinding;
    }

    public void setUmlmodel_templatebinding(UMLModel_TemplateBinding umlmodel_templatebinding) {
        this.umlmodel_templatebinding = umlmodel_templatebinding;
    }
    public List<UMLModel_ParameterableElement> getUmlmodel_parameterableelements() {
        return umlmodel_parameterableelements;
    }

    public void addUmlmodel_parameterableelement(Umlmodel_parameterableelement umlmodel_parameterableelement) {
        this.umlmodel_parameterableelements.add(umlmodel_parameterableelement);
    }

}