





import java.util.List;
import java.util.ArrayList;

public class pivot_TemplateSignature extends Element {






    private pivot_TemplateParameter pivot_templateparameter;




    private List<pivot_TemplateParameter> pivot_templateparameters;


    public pivot_TemplateSignature(
    ) {
        super(
        );
        this.pivot_templateparameters = new ArrayList<>();
    }

    public pivot_TemplateSignature(
        ArrayList<pivot_TemplateParameter> pivot_templateparameters    ) {
        this.pivot_templateparameters = pivot_templateparameters;
    }


    public pivot_TemplateParameter getPivot_templateparameter() {
        return pivot_templateparameter;
    }

    public void setPivot_templateparameter(pivot_TemplateParameter pivot_templateparameter) {
        this.pivot_templateparameter = pivot_templateparameter;
    }
    public List<pivot_TemplateParameter> getPivot_templateparameters() {
        return pivot_templateparameters;
    }

    public void addPivot_templateparameter(Pivot_templateparameter pivot_templateparameter) {
        this.pivot_templateparameters.add(pivot_templateparameter);
    }

}