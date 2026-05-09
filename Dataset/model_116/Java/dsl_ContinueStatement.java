





import java.util.List;
import java.util.ArrayList;

public class dsl_ContinueStatement  {

    private String id;





    private dsl_Statement dsl_statement;


    public dsl_ContinueStatement(
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

}