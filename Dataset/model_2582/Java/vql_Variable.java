





import java.util.List;
import java.util.ArrayList;

public class vql_Variable extends Expression {

    private String name;





    private vql_Pattern vql_pattern;




    private vql_VariableReference vql_variablereference;




    private vql_PatternBody vql_patternbody;


    public vql_Variable(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vql_Pattern getVql_pattern() {
        return vql_pattern;
    }

    public void setVql_pattern(vql_Pattern vql_pattern) {
        this.vql_pattern = vql_pattern;
    }
    public vql_VariableReference getVql_variablereference() {
        return vql_variablereference;
    }

    public void setVql_variablereference(vql_VariableReference vql_variablereference) {
        this.vql_variablereference = vql_variablereference;
    }
    public vql_PatternBody getVql_patternbody() {
        return vql_patternbody;
    }

    public void setVql_patternbody(vql_PatternBody vql_patternbody) {
        this.vql_patternbody = vql_patternbody;
    }

}