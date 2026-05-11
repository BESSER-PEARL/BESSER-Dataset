





import java.util.List;
import java.util.ArrayList;

public class myDsl_expression_statement extends statement {






    private myDsl_iteration_statement mydsl_iteration_statement;


    public myDsl_expression_statement(
    ) {
        super(
        );
    }



    public myDsl_iteration_statement getMydsl_iteration_statement() {
        return mydsl_iteration_statement;
    }

    public void setMydsl_iteration_statement(myDsl_iteration_statement mydsl_iteration_statement) {
        this.mydsl_iteration_statement = mydsl_iteration_statement;
    }

}