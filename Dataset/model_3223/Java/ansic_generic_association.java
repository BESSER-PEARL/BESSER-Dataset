





import java.util.List;
import java.util.ArrayList;

public class ansic_generic_association  {

    private String default;





    private ansic_assignment_expression ansic_assignment_expression;




    private ansic_generic_assoc_list ansic_generic_assoc_list;




    private ansic_type_name ansic_type_name;


    public ansic_generic_association(
        String default    ) {
        this.default = default;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public ansic_assignment_expression getAnsic_assignment_expression() {
        return ansic_assignment_expression;
    }

    public void setAnsic_assignment_expression(ansic_assignment_expression ansic_assignment_expression) {
        this.ansic_assignment_expression = ansic_assignment_expression;
    }
    public ansic_generic_assoc_list getAnsic_generic_assoc_list() {
        return ansic_generic_assoc_list;
    }

    public void setAnsic_generic_assoc_list(ansic_generic_assoc_list ansic_generic_assoc_list) {
        this.ansic_generic_assoc_list = ansic_generic_assoc_list;
    }
    public ansic_type_name getAnsic_type_name() {
        return ansic_type_name;
    }

    public void setAnsic_type_name(ansic_type_name ansic_type_name) {
        this.ansic_type_name = ansic_type_name;
    }

}