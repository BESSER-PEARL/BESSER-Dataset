





import java.util.List;
import java.util.ArrayList;

public class myDsl_postfix_expression  {






    private myDsl_type_name mydsl_type_name;




    private myDsl_simple_expression mydsl_simple_expression;


    public myDsl_postfix_expression(
    ) {
    }



    public myDsl_type_name getMydsl_type_name() {
        return mydsl_type_name;
    }

    public void setMydsl_type_name(myDsl_type_name mydsl_type_name) {
        this.mydsl_type_name = mydsl_type_name;
    }
    public myDsl_simple_expression getMydsl_simple_expression() {
        return mydsl_simple_expression;
    }

    public void setMydsl_simple_expression(myDsl_simple_expression mydsl_simple_expression) {
        this.mydsl_simple_expression = mydsl_simple_expression;
    }

}