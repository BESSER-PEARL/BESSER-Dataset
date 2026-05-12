





import java.util.List;
import java.util.ArrayList;

public class UML2_TemplateBinding extends DirectedRelationship {






    private UML2_TemplateableElement uml2_templateableelement;




    private UML2_TemplateParameterSubstitution uml2_templateparametersubstitution;




    private List<UML2_TemplateParameterSubstitution> uml2_templateparametersubstitutions;




    private UML2_TemplateSignature uml2_templatesignature;




    private UML2_TemplateableElement uml2_templateableelement;


    public UML2_TemplateBinding(
    ) {
        super(
        );
        this.uml2_templateparametersubstitutions = new ArrayList<>();
    }

    public UML2_TemplateBinding(
        ArrayList<UML2_TemplateParameterSubstitution> uml2_templateparametersubstitutions    ) {
        this.uml2_templateparametersubstitutions = uml2_templateparametersubstitutions;
    }


    public UML2_TemplateableElement getUml2_templateableelement() {
        return uml2_templateableelement;
    }

    public void setUml2_templateableelement(UML2_TemplateableElement uml2_templateableelement) {
        this.uml2_templateableelement = uml2_templateableelement;
    }
    public UML2_TemplateParameterSubstitution getUml2_templateparametersubstitution() {
        return uml2_templateparametersubstitution;
    }

    public void setUml2_templateparametersubstitution(UML2_TemplateParameterSubstitution uml2_templateparametersubstitution) {
        this.uml2_templateparametersubstitution = uml2_templateparametersubstitution;
    }
    public List<UML2_TemplateParameterSubstitution> getUml2_templateparametersubstitutions() {
        return uml2_templateparametersubstitutions;
    }

    public void addUml2_templateparametersubstitution(Uml2_templateparametersubstitution uml2_templateparametersubstitution) {
        this.uml2_templateparametersubstitutions.add(uml2_templateparametersubstitution);
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

}