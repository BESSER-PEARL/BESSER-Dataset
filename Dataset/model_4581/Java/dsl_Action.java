





import java.util.List;
import java.util.ArrayList;

public class dsl_Action  {

    private String name;





    private dsl_Try dsl_try;




    private dsl_Finally dsl_finally;




    private dsl_Catch dsl_catch;




    private dsl_Expression dsl_expression;


    public dsl_Action(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Try getDsl_try() {
        return dsl_try;
    }

    public void setDsl_try(dsl_Try dsl_try) {
        this.dsl_try = dsl_try;
    }
    public dsl_Finally getDsl_finally() {
        return dsl_finally;
    }

    public void setDsl_finally(dsl_Finally dsl_finally) {
        this.dsl_finally = dsl_finally;
    }
    public dsl_Catch getDsl_catch() {
        return dsl_catch;
    }

    public void setDsl_catch(dsl_Catch dsl_catch) {
        this.dsl_catch = dsl_catch;
    }
    public dsl_Expression getDsl_expression() {
        return dsl_expression;
    }

    public void setDsl_expression(dsl_Expression dsl_expression) {
        this.dsl_expression = dsl_expression;
    }

}