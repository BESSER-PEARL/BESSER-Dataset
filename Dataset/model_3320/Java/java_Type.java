





import java.util.List;
import java.util.ArrayList;

public class java_Type  {

    private String name;





    private java_Method_declaration java_method_declaration;




    private java_Variable_declaration java_variable_declaration;




    private java_Parameter java_parameter;


    public java_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public java_Method_declaration getJava_method_declaration() {
        return java_method_declaration;
    }

    public void setJava_method_declaration(java_Method_declaration java_method_declaration) {
        this.java_method_declaration = java_method_declaration;
    }
    public java_Variable_declaration getJava_variable_declaration() {
        return java_variable_declaration;
    }

    public void setJava_variable_declaration(java_Variable_declaration java_variable_declaration) {
        this.java_variable_declaration = java_variable_declaration;
    }
    public java_Parameter getJava_parameter() {
        return java_parameter;
    }

    public void setJava_parameter(java_Parameter java_parameter) {
        this.java_parameter = java_parameter;
    }

}