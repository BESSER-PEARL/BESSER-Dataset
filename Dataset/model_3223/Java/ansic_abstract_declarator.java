





import java.util.List;
import java.util.ArrayList;

public class ansic_abstract_declarator  {






    private ansic_pointer ansic_pointer;




    private ansic_type_name ansic_type_name;




    private ansic_parameter_declaration ansic_parameter_declaration;


    public ansic_abstract_declarator(
    ) {
    }



    public ansic_pointer getAnsic_pointer() {
        return ansic_pointer;
    }

    public void setAnsic_pointer(ansic_pointer ansic_pointer) {
        this.ansic_pointer = ansic_pointer;
    }
    public ansic_type_name getAnsic_type_name() {
        return ansic_type_name;
    }

    public void setAnsic_type_name(ansic_type_name ansic_type_name) {
        this.ansic_type_name = ansic_type_name;
    }
    public ansic_parameter_declaration getAnsic_parameter_declaration() {
        return ansic_parameter_declaration;
    }

    public void setAnsic_parameter_declaration(ansic_parameter_declaration ansic_parameter_declaration) {
        this.ansic_parameter_declaration = ansic_parameter_declaration;
    }

}