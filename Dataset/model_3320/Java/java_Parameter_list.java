





import java.util.List;
import java.util.ArrayList;

public class java_Parameter_list  {






    private java_Method_declaration java_method_declaration;




    private List<java_Parameter> java_parameters;




    private java_Constructor_declaration java_constructor_declaration;




    private java_Parameter java_parameter;


    public java_Parameter_list(
    ) {
        this.java_parameters = new ArrayList<>();
    }

    public java_Parameter_list(
        ArrayList<java_Parameter> java_parameters    ) {
        this.java_parameters = java_parameters;
    }


    public java_Method_declaration getJava_method_declaration() {
        return java_method_declaration;
    }

    public void setJava_method_declaration(java_Method_declaration java_method_declaration) {
        this.java_method_declaration = java_method_declaration;
    }
    public List<java_Parameter> getJava_parameters() {
        return java_parameters;
    }

    public void addJava_parameter(Java_parameter java_parameter) {
        this.java_parameters.add(java_parameter);
    }
    public java_Constructor_declaration getJava_constructor_declaration() {
        return java_constructor_declaration;
    }

    public void setJava_constructor_declaration(java_Constructor_declaration java_constructor_declaration) {
        this.java_constructor_declaration = java_constructor_declaration;
    }
    public java_Parameter getJava_parameter() {
        return java_parameter;
    }

    public void setJava_parameter(java_Parameter java_parameter) {
        this.java_parameter = java_parameter;
    }

}