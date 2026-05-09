





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_TemplateBinding extends DirectedRelationship {






    private UML2WithID_TemplateSignature uml2withid_templatesignature;




    private UML2WithID_TemplateParameterSubstitution uml2withid_templateparametersubstitution;




    private List<UML2WithID_TemplateParameterSubstitution> uml2withid_templateparametersubstitutions;




    private UML2WithID_TemplateableElement uml2withid_templateableelement;




    private UML2WithID_TemplateableElement uml2withid_templateableelement;


    public UML2WithID_TemplateBinding(
    ) {
        super(
        );
        this.uml2withid_templateparametersubstitutions = new ArrayList<>();
    }

    public UML2WithID_TemplateBinding(
        ArrayList<UML2WithID_TemplateParameterSubstitution> uml2withid_templateparametersubstitutions    ) {
        this.uml2withid_templateparametersubstitutions = uml2withid_templateparametersubstitutions;
    }


    public UML2WithID_TemplateSignature getUml2withid_templatesignature() {
        return uml2withid_templatesignature;
    }

    public void setUml2withid_templatesignature(UML2WithID_TemplateSignature uml2withid_templatesignature) {
        this.uml2withid_templatesignature = uml2withid_templatesignature;
    }
    public UML2WithID_TemplateParameterSubstitution getUml2withid_templateparametersubstitution() {
        return uml2withid_templateparametersubstitution;
    }

    public void setUml2withid_templateparametersubstitution(UML2WithID_TemplateParameterSubstitution uml2withid_templateparametersubstitution) {
        this.uml2withid_templateparametersubstitution = uml2withid_templateparametersubstitution;
    }
    public List<UML2WithID_TemplateParameterSubstitution> getUml2withid_templateparametersubstitutions() {
        return uml2withid_templateparametersubstitutions;
    }

    public void addUml2withid_templateparametersubstitution(Uml2withid_templateparametersubstitution uml2withid_templateparametersubstitution) {
        this.uml2withid_templateparametersubstitutions.add(uml2withid_templateparametersubstitution);
    }
    public UML2WithID_TemplateableElement getUml2withid_templateableelement() {
        return uml2withid_templateableelement;
    }

    public void setUml2withid_templateableelement(UML2WithID_TemplateableElement uml2withid_templateableelement) {
        this.uml2withid_templateableelement = uml2withid_templateableelement;
    }
    public UML2WithID_TemplateableElement getUml2withid_templateableelement() {
        return uml2withid_templateableelement;
    }

    public void setUml2withid_templateableelement(UML2WithID_TemplateableElement uml2withid_templateableelement) {
        this.uml2withid_templateableelement = uml2withid_templateableelement;
    }

}