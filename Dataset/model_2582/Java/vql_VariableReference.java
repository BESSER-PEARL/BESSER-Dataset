





import java.util.List;
import java.util.ArrayList;

public class vql_VariableReference extends ValueReference {

    private boolean aggregator;
    private String var;





    private vql_PathExpressionConstraint vql_pathexpressionconstraint;




    private vql_UnaryTypeConstraint vql_unarytypeconstraint;


    public vql_VariableReference(
        boolean aggregator,        String var    ) {
        super(
        );
        this.aggregator = aggregator;
        this.var = var;
    }


    public boolean getAggregator() {
        return aggregator;
    }

    public void setAggregator(boolean aggregator) {
        this.aggregator = aggregator;
    }
    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }

    public vql_PathExpressionConstraint getVql_pathexpressionconstraint() {
        return vql_pathexpressionconstraint;
    }

    public void setVql_pathexpressionconstraint(vql_PathExpressionConstraint vql_pathexpressionconstraint) {
        this.vql_pathexpressionconstraint = vql_pathexpressionconstraint;
    }
    public vql_UnaryTypeConstraint getVql_unarytypeconstraint() {
        return vql_unarytypeconstraint;
    }

    public void setVql_unarytypeconstraint(vql_UnaryTypeConstraint vql_unarytypeconstraint) {
        this.vql_unarytypeconstraint = vql_unarytypeconstraint;
    }

}