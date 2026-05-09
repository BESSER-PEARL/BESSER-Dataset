





import java.util.List;
import java.util.ArrayList;

public class QVTRelation_Relation extends Rule {

    private String isTopLevel;





    private Pattern pattern;




    private Pattern pattern;




    private List<Variable> variables;


    public QVTRelation_Relation(
        String isTopLevel    ) {
        super(
        );
        this.isTopLevel = isTopLevel;
        this.variables = new ArrayList<>();
    }

    public QVTRelation_Relation(
        String isTopLevel        ArrayList<Variable> variables    ) {
        this.isTopLevel = isTopLevel;
        this.variables = variables;
    }

    public String getIstoplevel() {
        return isTopLevel;
    }

    public void setIstoplevel(String isTopLevel) {
        this.isTopLevel = isTopLevel;
    }

    public Pattern getPattern() {
        return pattern;
    }

    public void setPattern(Pattern pattern) {
        this.pattern = pattern;
    }
    public Pattern getPattern() {
        return pattern;
    }

    public void setPattern(Pattern pattern) {
        this.pattern = pattern;
    }
    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}