





import java.util.List;
import java.util.ArrayList;

public class myDsl_init_declarator  {






    private myDsl_simple_expression mydsl_simple_expression;




    private myDsl_init_declarator_list mydsl_init_declarator_list;


    public myDsl_init_declarator(
    ) {
    }



    public myDsl_simple_expression getMydsl_simple_expression() {
        return mydsl_simple_expression;
    }

    public void setMydsl_simple_expression(myDsl_simple_expression mydsl_simple_expression) {
        this.mydsl_simple_expression = mydsl_simple_expression;
    }
    public myDsl_init_declarator_list getMydsl_init_declarator_list() {
        return mydsl_init_declarator_list;
    }

    public void setMydsl_init_declarator_list(myDsl_init_declarator_list mydsl_init_declarator_list) {
        this.mydsl_init_declarator_list = mydsl_init_declarator_list;
    }

}