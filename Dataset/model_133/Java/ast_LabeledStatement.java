





import java.util.List;
import java.util.ArrayList;

public class ast_LabeledStatement extends MethodContentStatement {






    private ast_Label ast_label;


    public ast_LabeledStatement(
    ) {
        super(
        );
    }



    public ast_Label getAst_label() {
        return ast_label;
    }

    public void setAst_label(ast_Label ast_label) {
        this.ast_label = ast_label;
    }

}