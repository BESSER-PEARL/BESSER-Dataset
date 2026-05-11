





import java.util.List;
import java.util.ArrayList;

public class pascal_ElementList  {






    private List<pascal_expression> pascal_expressions;




    private pascal_Set pascal_set;


    public pascal_ElementList(
    ) {
        this.pascal_expressions = new ArrayList<>();
    }

    public pascal_ElementList(
        ArrayList<pascal_expression> pascal_expressions    ) {
        this.pascal_expressions = pascal_expressions;
    }


    public List<pascal_expression> getPascal_expressions() {
        return pascal_expressions;
    }

    public void addPascal_expression(Pascal_expression pascal_expression) {
        this.pascal_expressions.add(pascal_expression);
    }
    public pascal_Set getPascal_set() {
        return pascal_set;
    }

    public void setPascal_set(pascal_Set pascal_set) {
        this.pascal_set = pascal_set;
    }

}