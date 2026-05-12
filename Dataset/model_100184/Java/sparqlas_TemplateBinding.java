





import java.util.List;
import java.util.ArrayList;

public class sparqlas_TemplateBinding  {






    private sparqlas_TemplateParameterSubstitution sparqlas_templateparametersubstitution;




    private List<sparqlas_TemplateParameterSubstitution> sparqlas_templateparametersubstitutions;




    private sparqlas_TemplateableElement sparqlas_templateableelement;




    private sparqlas_TemplateableElement sparqlas_templateableelement;




    private sparqlas_TemplateSignature sparqlas_templatesignature;


    public sparqlas_TemplateBinding(
    ) {
        this.sparqlas_templateparametersubstitutions = new ArrayList<>();
    }

    public sparqlas_TemplateBinding(
        ArrayList<sparqlas_TemplateParameterSubstitution> sparqlas_templateparametersubstitutions    ) {
        this.sparqlas_templateparametersubstitutions = sparqlas_templateparametersubstitutions;
    }


    public sparqlas_TemplateParameterSubstitution getSparqlas_templateparametersubstitution() {
        return sparqlas_templateparametersubstitution;
    }

    public void setSparqlas_templateparametersubstitution(sparqlas_TemplateParameterSubstitution sparqlas_templateparametersubstitution) {
        this.sparqlas_templateparametersubstitution = sparqlas_templateparametersubstitution;
    }
    public List<sparqlas_TemplateParameterSubstitution> getSparqlas_templateparametersubstitutions() {
        return sparqlas_templateparametersubstitutions;
    }

    public void addSparqlas_templateparametersubstitution(Sparqlas_templateparametersubstitution sparqlas_templateparametersubstitution) {
        this.sparqlas_templateparametersubstitutions.add(sparqlas_templateparametersubstitution);
    }
    public sparqlas_TemplateableElement getSparqlas_templateableelement() {
        return sparqlas_templateableelement;
    }

    public void setSparqlas_templateableelement(sparqlas_TemplateableElement sparqlas_templateableelement) {
        this.sparqlas_templateableelement = sparqlas_templateableelement;
    }
    public sparqlas_TemplateableElement getSparqlas_templateableelement() {
        return sparqlas_templateableelement;
    }

    public void setSparqlas_templateableelement(sparqlas_TemplateableElement sparqlas_templateableelement) {
        this.sparqlas_templateableelement = sparqlas_templateableelement;
    }
    public sparqlas_TemplateSignature getSparqlas_templatesignature() {
        return sparqlas_templatesignature;
    }

    public void setSparqlas_templatesignature(sparqlas_TemplateSignature sparqlas_templatesignature) {
        this.sparqlas_templatesignature = sparqlas_templatesignature;
    }

}