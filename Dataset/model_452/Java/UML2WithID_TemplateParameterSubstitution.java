





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_TemplateParameterSubstitution extends Element {






    private UML2WithID_TemplateBinding uml2withid_templatebinding;




    private List<UML2WithID_ParameterableElement> uml2withid_parameterableelements;




    private UML2WithID_TemplateBinding uml2withid_templatebinding;




    private UML2WithID_TemplateParameter uml2withid_templateparameter;




    private List<UML2WithID_ParameterableElement> uml2withid_parameterableelements;


    public UML2WithID_TemplateParameterSubstitution(
    ) {
        super(
        );
        this.uml2withid_parameterableelements = new ArrayList<>();
        this.uml2withid_parameterableelements = new ArrayList<>();
    }

    public UML2WithID_TemplateParameterSubstitution(
        ArrayList<UML2WithID_ParameterableElement> uml2withid_parameterableelements,        ArrayList<UML2WithID_ParameterableElement> uml2withid_parameterableelements    ) {
        this.uml2withid_parameterableelements = uml2withid_parameterableelements;
        this.uml2withid_parameterableelements = uml2withid_parameterableelements;
    }


    public UML2WithID_TemplateBinding getUml2withid_templatebinding() {
        return uml2withid_templatebinding;
    }

    public void setUml2withid_templatebinding(UML2WithID_TemplateBinding uml2withid_templatebinding) {
        this.uml2withid_templatebinding = uml2withid_templatebinding;
    }
    public List<UML2WithID_ParameterableElement> getUml2withid_parameterableelements() {
        return uml2withid_parameterableelements;
    }

    public void addUml2withid_parameterableelement(Uml2withid_parameterableelement uml2withid_parameterableelement) {
        this.uml2withid_parameterableelements.add(uml2withid_parameterableelement);
    }
    public UML2WithID_TemplateBinding getUml2withid_templatebinding() {
        return uml2withid_templatebinding;
    }

    public void setUml2withid_templatebinding(UML2WithID_TemplateBinding uml2withid_templatebinding) {
        this.uml2withid_templatebinding = uml2withid_templatebinding;
    }
    public UML2WithID_TemplateParameter getUml2withid_templateparameter() {
        return uml2withid_templateparameter;
    }

    public void setUml2withid_templateparameter(UML2WithID_TemplateParameter uml2withid_templateparameter) {
        this.uml2withid_templateparameter = uml2withid_templateparameter;
    }
    public List<UML2WithID_ParameterableElement> getUml2withid_parameterableelements() {
        return uml2withid_parameterableelements;
    }

    public void addUml2withid_parameterableelement(Uml2withid_parameterableelement uml2withid_parameterableelement) {
        this.uml2withid_parameterableelements.add(uml2withid_parameterableelement);
    }

}