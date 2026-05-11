





import java.util.List;
import java.util.ArrayList;

public class myDsl_struct_declarator  {






    private myDsl_declarator mydsl_declarator;




    private myDsl_constant_expression mydsl_constant_expression;




    private myDsl_struct_declarator_list mydsl_struct_declarator_list;


    public myDsl_struct_declarator(
    ) {
    }



    public myDsl_declarator getMydsl_declarator() {
        return mydsl_declarator;
    }

    public void setMydsl_declarator(myDsl_declarator mydsl_declarator) {
        this.mydsl_declarator = mydsl_declarator;
    }
    public myDsl_constant_expression getMydsl_constant_expression() {
        return mydsl_constant_expression;
    }

    public void setMydsl_constant_expression(myDsl_constant_expression mydsl_constant_expression) {
        this.mydsl_constant_expression = mydsl_constant_expression;
    }
    public myDsl_struct_declarator_list getMydsl_struct_declarator_list() {
        return mydsl_struct_declarator_list;
    }

    public void setMydsl_struct_declarator_list(myDsl_struct_declarator_list mydsl_struct_declarator_list) {
        this.mydsl_struct_declarator_list = mydsl_struct_declarator_list;
    }

}