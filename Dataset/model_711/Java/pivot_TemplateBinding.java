





import java.util.List;
import java.util.ArrayList;

public class pivot_TemplateBinding extends Element {






    private pivot_TemplateableElement pivot_templateableelement;




    private pivot_TemplateParameterSubstitution pivot_templateparametersubstitution;




    private List<pivot_TemplateParameterSubstitution> pivot_templateparametersubstitutions;




    private pivot_TemplateSignature pivot_templatesignature;




    private pivot_TemplateableElement pivot_templateableelement;


    public pivot_TemplateBinding(
    ) {
        super(
        );
        this.pivot_templateparametersubstitutions = new ArrayList<>();
    }

    public pivot_TemplateBinding(
        ArrayList<pivot_TemplateParameterSubstitution> pivot_templateparametersubstitutions    ) {
        this.pivot_templateparametersubstitutions = pivot_templateparametersubstitutions;
    }


    public pivot_TemplateableElement getPivot_templateableelement() {
        return pivot_templateableelement;
    }

    public void setPivot_templateableelement(pivot_TemplateableElement pivot_templateableelement) {
        this.pivot_templateableelement = pivot_templateableelement;
    }
    public pivot_TemplateParameterSubstitution getPivot_templateparametersubstitution() {
        return pivot_templateparametersubstitution;
    }

    public void setPivot_templateparametersubstitution(pivot_TemplateParameterSubstitution pivot_templateparametersubstitution) {
        this.pivot_templateparametersubstitution = pivot_templateparametersubstitution;
    }
    public List<pivot_TemplateParameterSubstitution> getPivot_templateparametersubstitutions() {
        return pivot_templateparametersubstitutions;
    }

    public void addPivot_templateparametersubstitution(Pivot_templateparametersubstitution pivot_templateparametersubstitution) {
        this.pivot_templateparametersubstitutions.add(pivot_templateparametersubstitution);
    }
    public pivot_TemplateSignature getPivot_templatesignature() {
        return pivot_templatesignature;
    }

    public void setPivot_templatesignature(pivot_TemplateSignature pivot_templatesignature) {
        this.pivot_templatesignature = pivot_templatesignature;
    }
    public pivot_TemplateableElement getPivot_templateableelement() {
        return pivot_templateableelement;
    }

    public void setPivot_templateableelement(pivot_TemplateableElement pivot_templateableelement) {
        this.pivot_templateableelement = pivot_templateableelement;
    }

}