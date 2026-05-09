





import java.util.List;
import java.util.ArrayList;

public class uml_TemplateBinding extends DirectedRelationship {






    private uml_TemplateSignature uml_templatesignature;




    private uml_TemplateParameterSubstitution uml_templateparametersubstitution;




    private uml_TemplateableElement uml_templateableelement;




    private List<uml_TemplateParameterSubstitution> uml_templateparametersubstitutions;




    private uml_TemplateableElement uml_templateableelement;


    public uml_TemplateBinding(
    ) {
        super(
        );
        this.uml_templateparametersubstitutions = new ArrayList<>();
    }

    public uml_TemplateBinding(
        ArrayList<uml_TemplateParameterSubstitution> uml_templateparametersubstitutions    ) {
        this.uml_templateparametersubstitutions = uml_templateparametersubstitutions;
    }


    public uml_TemplateSignature getUml_templatesignature() {
        return uml_templatesignature;
    }

    public void setUml_templatesignature(uml_TemplateSignature uml_templatesignature) {
        this.uml_templatesignature = uml_templatesignature;
    }
    public uml_TemplateParameterSubstitution getUml_templateparametersubstitution() {
        return uml_templateparametersubstitution;
    }

    public void setUml_templateparametersubstitution(uml_TemplateParameterSubstitution uml_templateparametersubstitution) {
        this.uml_templateparametersubstitution = uml_templateparametersubstitution;
    }
    public uml_TemplateableElement getUml_templateableelement() {
        return uml_templateableelement;
    }

    public void setUml_templateableelement(uml_TemplateableElement uml_templateableelement) {
        this.uml_templateableelement = uml_templateableelement;
    }
    public List<uml_TemplateParameterSubstitution> getUml_templateparametersubstitutions() {
        return uml_templateparametersubstitutions;
    }

    public void addUml_templateparametersubstitution(Uml_templateparametersubstitution uml_templateparametersubstitution) {
        this.uml_templateparametersubstitutions.add(uml_templateparametersubstitution);
    }
    public uml_TemplateableElement getUml_templateableelement() {
        return uml_templateableelement;
    }

    public void setUml_templateableelement(uml_TemplateableElement uml_templateableelement) {
        this.uml_templateableelement = uml_templateableelement;
    }

}