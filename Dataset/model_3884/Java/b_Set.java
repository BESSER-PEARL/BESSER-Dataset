





import java.util.List;
import java.util.ArrayList;

public class b_Set  {






    private b_Variable b_variable;




    private List<b_Variable> b_variables;




    private b_Sets b_sets;


    public b_Set(
    ) {
        this.b_variables = new ArrayList<>();
    }

    public b_Set(
        ArrayList<b_Variable> b_variables    ) {
        this.b_variables = b_variables;
    }


    public b_Variable getB_variable() {
        return b_variable;
    }

    public void setB_variable(b_Variable b_variable) {
        this.b_variable = b_variable;
    }
    public List<b_Variable> getB_variables() {
        return b_variables;
    }

    public void addB_variable(B_variable b_variable) {
        this.b_variables.add(b_variable);
    }
    public b_Sets getB_sets() {
        return b_sets;
    }

    public void setB_sets(b_Sets b_sets) {
        this.b_sets = b_sets;
    }

}