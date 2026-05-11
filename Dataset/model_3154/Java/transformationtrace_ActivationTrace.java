





import java.util.List;
import java.util.ArrayList;

public class transformationtrace_ActivationTrace  {

    private String ruleName;





    private List<transformationtrace_RuleParameterTrace> transformationtrace_ruleparametertraces;




    private transformationtrace_TransformationTrace transformationtrace_transformationtrace;


    public transformationtrace_ActivationTrace(
        String ruleName    ) {
        this.ruleName = ruleName;
        this.transformationtrace_ruleparametertraces = new ArrayList<>();
    }

    public transformationtrace_ActivationTrace(
        String ruleName        ArrayList<transformationtrace_RuleParameterTrace> transformationtrace_ruleparametertraces    ) {
        this.ruleName = ruleName;
        this.transformationtrace_ruleparametertraces = transformationtrace_ruleparametertraces;
    }

    public String getRulename() {
        return ruleName;
    }

    public void setRulename(String ruleName) {
        this.ruleName = ruleName;
    }

    public List<transformationtrace_RuleParameterTrace> getTransformationtrace_ruleparametertraces() {
        return transformationtrace_ruleparametertraces;
    }

    public void addTransformationtrace_ruleparametertrace(Transformationtrace_ruleparametertrace transformationtrace_ruleparametertrace) {
        this.transformationtrace_ruleparametertraces.add(transformationtrace_ruleparametertrace);
    }
    public transformationtrace_TransformationTrace getTransformationtrace_transformationtrace() {
        return transformationtrace_transformationtrace;
    }

    public void setTransformationtrace_transformationtrace(transformationtrace_TransformationTrace transformationtrace_transformationtrace) {
        this.transformationtrace_transformationtrace = transformationtrace_transformationtrace;
    }

}