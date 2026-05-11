





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Design  {

    private String DoE;





    private List<jpdl31_Factor> jpdl31_factors;




    private List<jpdl31_DependentVariable> jpdl31_dependentvariables;




    private List<jpdl31_Parameter> jpdl31_parameters;




    private jpdl31_ExperimentalPlan jpdl31_experimentalplan;


    public jpdl31_Design(
        String DoE    ) {
        this.DoE = DoE;
        this.jpdl31_factors = new ArrayList<>();
        this.jpdl31_dependentvariables = new ArrayList<>();
        this.jpdl31_parameters = new ArrayList<>();
    }

    public jpdl31_Design(
        String DoE        ArrayList<jpdl31_Factor> jpdl31_factors,        ArrayList<jpdl31_DependentVariable> jpdl31_dependentvariables,        ArrayList<jpdl31_Parameter> jpdl31_parameters    ) {
        this.DoE = DoE;
        this.jpdl31_factors = jpdl31_factors;
        this.jpdl31_dependentvariables = jpdl31_dependentvariables;
        this.jpdl31_parameters = jpdl31_parameters;
    }

    public String getDoe() {
        return DoE;
    }

    public void setDoe(String DoE) {
        this.DoE = DoE;
    }

    public List<jpdl31_Factor> getJpdl31_factors() {
        return jpdl31_factors;
    }

    public void addJpdl31_factor(Jpdl31_factor jpdl31_factor) {
        this.jpdl31_factors.add(jpdl31_factor);
    }
    public List<jpdl31_DependentVariable> getJpdl31_dependentvariables() {
        return jpdl31_dependentvariables;
    }

    public void addJpdl31_dependentvariable(Jpdl31_dependentvariable jpdl31_dependentvariable) {
        this.jpdl31_dependentvariables.add(jpdl31_dependentvariable);
    }
    public List<jpdl31_Parameter> getJpdl31_parameters() {
        return jpdl31_parameters;
    }

    public void addJpdl31_parameter(Jpdl31_parameter jpdl31_parameter) {
        this.jpdl31_parameters.add(jpdl31_parameter);
    }
    public jpdl31_ExperimentalPlan getJpdl31_experimentalplan() {
        return jpdl31_experimentalplan;
    }

    public void setJpdl31_experimentalplan(jpdl31_ExperimentalPlan jpdl31_experimentalplan) {
        this.jpdl31_experimentalplan = jpdl31_experimentalplan;
    }

}