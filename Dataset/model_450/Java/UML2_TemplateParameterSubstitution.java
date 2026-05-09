





import java.util.List;
import java.util.ArrayList;

public class UML2_TemplateParameterSubstitution extends Element {






    private UML2_TemplateBinding uml2_templatebinding;




    private UML2_TemplateBinding uml2_templatebinding;




    private UML2_TemplateParameter uml2_templateparameter;




    private List<UML2_ParameterableElement> uml2_parameterableelements;




    private List<UML2_ParameterableElement> uml2_parameterableelements;


    public UML2_TemplateParameterSubstitution(
    ) {
        super(
        );
        this.uml2_parameterableelements = new ArrayList<>();
        this.uml2_parameterableelements = new ArrayList<>();
    }

    public UML2_TemplateParameterSubstitution(
        ArrayList<UML2_ParameterableElement> uml2_parameterableelements,        ArrayList<UML2_ParameterableElement> uml2_parameterableelements    ) {
        this.uml2_parameterableelements = uml2_parameterableelements;
        this.uml2_parameterableelements = uml2_parameterableelements;
    }


    public UML2_TemplateBinding getUml2_templatebinding() {
        return uml2_templatebinding;
    }

    public void setUml2_templatebinding(UML2_TemplateBinding uml2_templatebinding) {
        this.uml2_templatebinding = uml2_templatebinding;
    }
    public UML2_TemplateBinding getUml2_templatebinding() {
        return uml2_templatebinding;
    }

    public void setUml2_templatebinding(UML2_TemplateBinding uml2_templatebinding) {
        this.uml2_templatebinding = uml2_templatebinding;
    }
    public UML2_TemplateParameter getUml2_templateparameter() {
        return uml2_templateparameter;
    }

    public void setUml2_templateparameter(UML2_TemplateParameter uml2_templateparameter) {
        this.uml2_templateparameter = uml2_templateparameter;
    }
    public List<UML2_ParameterableElement> getUml2_parameterableelements() {
        return uml2_parameterableelements;
    }

    public void addUml2_parameterableelement(Uml2_parameterableelement uml2_parameterableelement) {
        this.uml2_parameterableelements.add(uml2_parameterableelement);
    }
    public List<UML2_ParameterableElement> getUml2_parameterableelements() {
        return uml2_parameterableelements;
    }

    public void addUml2_parameterableelement(Uml2_parameterableelement uml2_parameterableelement) {
        this.uml2_parameterableelements.add(uml2_parameterableelement);
    }

}