





import java.util.List;
import java.util.ArrayList;

public class dsl_ForStatement  {

    private String id;





    private dsl_Statement dsl_statement;




    private dsl_Expression dsl_expression;




    private dsl_Statement dsl_statement;




    private dsl_Expression dsl_expression;




    private dsl_Type dsl_type;


    public dsl_ForStatement(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dsl_Statement getDsl_statement() {
        return dsl_statement;
    }

    public void setDsl_statement(dsl_Statement dsl_statement) {
        this.dsl_statement = dsl_statement;
    }
    public dsl_Expression getDsl_expression() {
        return dsl_expression;
    }

    public void setDsl_expression(dsl_Expression dsl_expression) {
        this.dsl_expression = dsl_expression;
    }
    public dsl_Statement getDsl_statement() {
        return dsl_statement;
    }

    public void setDsl_statement(dsl_Statement dsl_statement) {
        this.dsl_statement = dsl_statement;
    }
    public dsl_Expression getDsl_expression() {
        return dsl_expression;
    }

    public void setDsl_expression(dsl_Expression dsl_expression) {
        this.dsl_expression = dsl_expression;
    }
    public dsl_Type getDsl_type() {
        return dsl_type;
    }

    public void setDsl_type(dsl_Type dsl_type) {
        this.dsl_type = dsl_type;
    }

}