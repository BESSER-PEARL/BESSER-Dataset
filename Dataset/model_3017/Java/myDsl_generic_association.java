





import java.util.List;
import java.util.ArrayList;

public class myDsl_generic_association  {

    private String default;





    private myDsl_type_name mydsl_type_name;




    private myDsl_assignment_expression mydsl_assignment_expression;




    private myDsl_generic_assoc_list mydsl_generic_assoc_list;




    private myDsl_generic_assoc_list mydsl_generic_assoc_list;


    public myDsl_generic_association(
        String default    ) {
        this.default = default;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public myDsl_type_name getMydsl_type_name() {
        return mydsl_type_name;
    }

    public void setMydsl_type_name(myDsl_type_name mydsl_type_name) {
        this.mydsl_type_name = mydsl_type_name;
    }
    public myDsl_assignment_expression getMydsl_assignment_expression() {
        return mydsl_assignment_expression;
    }

    public void setMydsl_assignment_expression(myDsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expression = mydsl_assignment_expression;
    }
    public myDsl_generic_assoc_list getMydsl_generic_assoc_list() {
        return mydsl_generic_assoc_list;
    }

    public void setMydsl_generic_assoc_list(myDsl_generic_assoc_list mydsl_generic_assoc_list) {
        this.mydsl_generic_assoc_list = mydsl_generic_assoc_list;
    }
    public myDsl_generic_assoc_list getMydsl_generic_assoc_list() {
        return mydsl_generic_assoc_list;
    }

    public void setMydsl_generic_assoc_list(myDsl_generic_assoc_list mydsl_generic_assoc_list) {
        this.mydsl_generic_assoc_list = mydsl_generic_assoc_list;
    }

}