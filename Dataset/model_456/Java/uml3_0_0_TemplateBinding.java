





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_TemplateBinding extends DirectedRelationship {






    private List<uml3_0_0_TemplateParameterSubstitution> uml3_0_0_templateparametersubstitutions;




    private uml3_0_0_TemplateParameterSubstitution uml3_0_0_templateparametersubstitution;




    private uml3_0_0_TemplateSignature uml3_0_0_templatesignature;




    private uml3_0_0_TemplateableElement uml3_0_0_templateableelement;




    private uml3_0_0_TemplateableElement uml3_0_0_templateableelement;


    public uml3_0_0_TemplateBinding(
    ) {
        super(
        );
        this.uml3_0_0_templateparametersubstitutions = new ArrayList<>();
    }

    public uml3_0_0_TemplateBinding(
        ArrayList<uml3_0_0_TemplateParameterSubstitution> uml3_0_0_templateparametersubstitutions    ) {
        this.uml3_0_0_templateparametersubstitutions = uml3_0_0_templateparametersubstitutions;
    }


    public List<uml3_0_0_TemplateParameterSubstitution> getUml3_0_0_templateparametersubstitutions() {
        return uml3_0_0_templateparametersubstitutions;
    }

    public void addUml3_0_0_templateparametersubstitution(Uml3_0_0_templateparametersubstitution uml3_0_0_templateparametersubstitution) {
        this.uml3_0_0_templateparametersubstitutions.add(uml3_0_0_templateparametersubstitution);
    }
    public uml3_0_0_TemplateParameterSubstitution getUml3_0_0_templateparametersubstitution() {
        return uml3_0_0_templateparametersubstitution;
    }

    public void setUml3_0_0_templateparametersubstitution(uml3_0_0_TemplateParameterSubstitution uml3_0_0_templateparametersubstitution) {
        this.uml3_0_0_templateparametersubstitution = uml3_0_0_templateparametersubstitution;
    }
    public uml3_0_0_TemplateSignature getUml3_0_0_templatesignature() {
        return uml3_0_0_templatesignature;
    }

    public void setUml3_0_0_templatesignature(uml3_0_0_TemplateSignature uml3_0_0_templatesignature) {
        this.uml3_0_0_templatesignature = uml3_0_0_templatesignature;
    }
    public uml3_0_0_TemplateableElement getUml3_0_0_templateableelement() {
        return uml3_0_0_templateableelement;
    }

    public void setUml3_0_0_templateableelement(uml3_0_0_TemplateableElement uml3_0_0_templateableelement) {
        this.uml3_0_0_templateableelement = uml3_0_0_templateableelement;
    }
    public uml3_0_0_TemplateableElement getUml3_0_0_templateableelement() {
        return uml3_0_0_templateableelement;
    }

    public void setUml3_0_0_templateableelement(uml3_0_0_TemplateableElement uml3_0_0_templateableelement) {
        this.uml3_0_0_templateableelement = uml3_0_0_templateableelement;
    }

}