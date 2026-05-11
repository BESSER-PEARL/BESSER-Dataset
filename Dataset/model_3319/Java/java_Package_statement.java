





import java.util.List;
import java.util.ArrayList;

public class java_Package_statement  {

    private String name;





    private java_Compilation_unit java_compilation_unit;


    public java_Package_statement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public java_Compilation_unit getJava_compilation_unit() {
        return java_compilation_unit;
    }

    public void setJava_compilation_unit(java_Compilation_unit java_compilation_unit) {
        this.java_compilation_unit = java_compilation_unit;
    }

}