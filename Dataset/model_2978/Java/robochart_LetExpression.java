





import java.util.List;
import java.util.ArrayList;

public class robochart_LetExpression extends Expression {






    private List<robochart_Declaration> robochart_declarations;


    public robochart_LetExpression(
    ) {
        super(
        );
        this.robochart_declarations = new ArrayList<>();
    }

    public robochart_LetExpression(
        ArrayList<robochart_Declaration> robochart_declarations    ) {
        this.robochart_declarations = robochart_declarations;
    }


    public List<robochart_Declaration> getRobochart_declarations() {
        return robochart_declarations;
    }

    public void addRobochart_declaration(Robochart_declaration robochart_declaration) {
        this.robochart_declarations.add(robochart_declaration);
    }

}