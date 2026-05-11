





import java.util.List;
import java.util.ArrayList;

public class vql_CallableRelation  {

    private String transitive;





    private vql_PatternCompositionConstraint vql_patterncompositionconstraint;


    public vql_CallableRelation(
        String transitive    ) {
        this.transitive = transitive;
    }


    public String getTransitive() {
        return transitive;
    }

    public void setTransitive(String transitive) {
        this.transitive = transitive;
    }

    public vql_PatternCompositionConstraint getVql_patterncompositionconstraint() {
        return vql_patterncompositionconstraint;
    }

    public void setVql_patterncompositionconstraint(vql_PatternCompositionConstraint vql_patterncompositionconstraint) {
        this.vql_patterncompositionconstraint = vql_patterncompositionconstraint;
    }

}