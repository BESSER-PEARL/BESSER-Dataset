





import java.util.List;
import java.util.ArrayList;

public class myDsl_Creating_Expression  {

    private String className;





    private myDsl_Type_specifier mydsl_type_specifier;




    private myDsl_Expression mydsl_expression;




    private myDsl_Arg_List mydsl_arg_list;




    private myDsl_Expression mydsl_expression;


    public myDsl_Creating_Expression(
        String className    ) {
        this.className = className;
    }


    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }

    public myDsl_Type_specifier getMydsl_type_specifier() {
        return mydsl_type_specifier;
    }

    public void setMydsl_type_specifier(myDsl_Type_specifier mydsl_type_specifier) {
        this.mydsl_type_specifier = mydsl_type_specifier;
    }
    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_Arg_List getMydsl_arg_list() {
        return mydsl_arg_list;
    }

    public void setMydsl_arg_list(myDsl_Arg_List mydsl_arg_list) {
        this.mydsl_arg_list = mydsl_arg_list;
    }
    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }

}