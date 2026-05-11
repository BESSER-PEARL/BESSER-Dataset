





import java.util.List;
import java.util.ArrayList;

public class robochart_Enumeration extends TypeDecl {






    private List<robochart_Literal> robochart_literals;


    public robochart_Enumeration(
    ) {
        super(
        );
        this.robochart_literals = new ArrayList<>();
    }

    public robochart_Enumeration(
        ArrayList<robochart_Literal> robochart_literals    ) {
        this.robochart_literals = robochart_literals;
    }


    public List<robochart_Literal> getRobochart_literals() {
        return robochart_literals;
    }

    public void addRobochart_literal(Robochart_literal robochart_literal) {
        this.robochart_literals.add(robochart_literal);
    }

}