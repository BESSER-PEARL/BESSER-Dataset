





import java.util.List;
import java.util.ArrayList;

public class myDsl_direct_abstract_declarator2  {

    private String static;





    private myDsl_direct_abstract_declarator mydsl_direct_abstract_declarator;




    private myDsl_assignment_expression mydsl_assignment_expression;




    private myDsl_type_qualifier_list mydsl_type_qualifier_list;




    private myDsl_parameter_type_list mydsl_parameter_type_list;


    public myDsl_direct_abstract_declarator2(
        String static    ) {
        this.static = static;
    }


    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }

    public myDsl_direct_abstract_declarator getMydsl_direct_abstract_declarator() {
        return mydsl_direct_abstract_declarator;
    }

    public void setMydsl_direct_abstract_declarator(myDsl_direct_abstract_declarator mydsl_direct_abstract_declarator) {
        this.mydsl_direct_abstract_declarator = mydsl_direct_abstract_declarator;
    }
    public myDsl_assignment_expression getMydsl_assignment_expression() {
        return mydsl_assignment_expression;
    }

    public void setMydsl_assignment_expression(myDsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expression = mydsl_assignment_expression;
    }
    public myDsl_type_qualifier_list getMydsl_type_qualifier_list() {
        return mydsl_type_qualifier_list;
    }

    public void setMydsl_type_qualifier_list(myDsl_type_qualifier_list mydsl_type_qualifier_list) {
        this.mydsl_type_qualifier_list = mydsl_type_qualifier_list;
    }
    public myDsl_parameter_type_list getMydsl_parameter_type_list() {
        return mydsl_parameter_type_list;
    }

    public void setMydsl_parameter_type_list(myDsl_parameter_type_list mydsl_parameter_type_list) {
        this.mydsl_parameter_type_list = mydsl_parameter_type_list;
    }

}