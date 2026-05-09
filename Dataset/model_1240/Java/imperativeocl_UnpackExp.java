





import java.util.List;
import java.util.ArrayList;

public class imperativeocl_UnpackExp extends ImperativeExpression {






    private List<imperativeocl_Variable> imperativeocl_variables;


    public imperativeocl_UnpackExp(
    ) {
        super(
        );
        this.imperativeocl_variables = new ArrayList<>();
    }

    public imperativeocl_UnpackExp(
        ArrayList<imperativeocl_Variable> imperativeocl_variables    ) {
        this.imperativeocl_variables = imperativeocl_variables;
    }


    public List<imperativeocl_Variable> getImperativeocl_variables() {
        return imperativeocl_variables;
    }

    public void addImperativeocl_variable(Imperativeocl_variable imperativeocl_variable) {
        this.imperativeocl_variables.add(imperativeocl_variable);
    }

}