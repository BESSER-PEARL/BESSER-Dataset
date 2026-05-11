





import java.util.List;
import java.util.ArrayList;

public class myDsl_struct_declarator  {






    private myDsl_struct_declarator_list mydsl_struct_declarator_list;




    private myDsl_constant_expression mydsl_constant_expression;


    public myDsl_struct_declarator(
    ) {
    }



    public myDsl_struct_declarator_list getMydsl_struct_declarator_list() {
        return mydsl_struct_declarator_list;
    }

    public void setMydsl_struct_declarator_list(myDsl_struct_declarator_list mydsl_struct_declarator_list) {
        this.mydsl_struct_declarator_list = mydsl_struct_declarator_list;
    }
    public myDsl_constant_expression getMydsl_constant_expression() {
        return mydsl_constant_expression;
    }

    public void setMydsl_constant_expression(myDsl_constant_expression mydsl_constant_expression) {
        this.mydsl_constant_expression = mydsl_constant_expression;
    }

}