





import java.util.List;
import java.util.ArrayList;

public class sparrow_Action  {

    private String name;





    private sparrow_Finally sparrow_finally;




    private sparrow_Expression sparrow_expression;




    private sparrow_Catch sparrow_catch;




    private sparrow_Try sparrow_try;


    public sparrow_Action(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sparrow_Finally getSparrow_finally() {
        return sparrow_finally;
    }

    public void setSparrow_finally(sparrow_Finally sparrow_finally) {
        this.sparrow_finally = sparrow_finally;
    }
    public sparrow_Expression getSparrow_expression() {
        return sparrow_expression;
    }

    public void setSparrow_expression(sparrow_Expression sparrow_expression) {
        this.sparrow_expression = sparrow_expression;
    }
    public sparrow_Catch getSparrow_catch() {
        return sparrow_catch;
    }

    public void setSparrow_catch(sparrow_Catch sparrow_catch) {
        this.sparrow_catch = sparrow_catch;
    }
    public sparrow_Try getSparrow_try() {
        return sparrow_try;
    }

    public void setSparrow_try(sparrow_Try sparrow_try) {
        this.sparrow_try = sparrow_try;
    }

}