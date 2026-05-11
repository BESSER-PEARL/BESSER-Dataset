





import java.util.List;
import java.util.ArrayList;

public class robochart_VariableList  {

    private String modifier;





    private List<robochart_Variable> robochart_variables;


    public robochart_VariableList(
        String modifier    ) {
        this.modifier = modifier;
        this.robochart_variables = new ArrayList<>();
    }

    public robochart_VariableList(
        String modifier        ArrayList<robochart_Variable> robochart_variables    ) {
        this.modifier = modifier;
        this.robochart_variables = robochart_variables;
    }

    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }

    public List<robochart_Variable> getRobochart_variables() {
        return robochart_variables;
    }

    public void addRobochart_variable(Robochart_variable robochart_variable) {
        this.robochart_variables.add(robochart_variable);
    }

}