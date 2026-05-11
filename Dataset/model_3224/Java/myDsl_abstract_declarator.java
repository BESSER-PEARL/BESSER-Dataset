





import java.util.List;
import java.util.ArrayList;

public class myDsl_abstract_declarator  {






    private myDsl_type_name mydsl_type_name;




    private myDsl_pointer mydsl_pointer;




    private myDsl_parameter_declaration mydsl_parameter_declaration;


    public myDsl_abstract_declarator(
    ) {
    }



    public myDsl_type_name getMydsl_type_name() {
        return mydsl_type_name;
    }

    public void setMydsl_type_name(myDsl_type_name mydsl_type_name) {
        this.mydsl_type_name = mydsl_type_name;
    }
    public myDsl_pointer getMydsl_pointer() {
        return mydsl_pointer;
    }

    public void setMydsl_pointer(myDsl_pointer mydsl_pointer) {
        this.mydsl_pointer = mydsl_pointer;
    }
    public myDsl_parameter_declaration getMydsl_parameter_declaration() {
        return mydsl_parameter_declaration;
    }

    public void setMydsl_parameter_declaration(myDsl_parameter_declaration mydsl_parameter_declaration) {
        this.mydsl_parameter_declaration = mydsl_parameter_declaration;
    }

}