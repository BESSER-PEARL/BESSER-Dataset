





import java.util.List;
import java.util.ArrayList;

public class java_Type  {

    private String name;





    private java_Method_declaration java_method_declaration;


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

}