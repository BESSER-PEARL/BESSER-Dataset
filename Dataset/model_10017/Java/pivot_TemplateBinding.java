





import java.util.List;
import java.util.ArrayList;

public class pivot_TemplateBinding extends Element {






    private List<pivot_TemplateParameterSubstitution> pivot_templateparametersubstitutions;




    private pivot_TemplateParameterSubstitution pivot_templateparametersubstitution;


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


    public List<pivot_TemplateParameterSubstitution> getPivot_templateparametersubstitutions() {
        return pivot_templateparametersubstitutions;
    }

    public void addPivot_templateparametersubstitution(Pivot_templateparametersubstitution pivot_templateparametersubstitution) {
        this.pivot_templateparametersubstitutions.add(pivot_templateparametersubstitution);
    }
    public pivot_TemplateParameterSubstitution getPivot_templateparametersubstitution() {
        return pivot_templateparametersubstitution;
    }

    public void setPivot_templateparametersubstitution(pivot_TemplateParameterSubstitution pivot_templateparametersubstitution) {
        this.pivot_templateparametersubstitution = pivot_templateparametersubstitution;
    }

}