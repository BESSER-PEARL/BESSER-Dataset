





import java.util.List;
import java.util.ArrayList;

public class java_Type_declaration  {

    private String doc;





    private java_Compilation_unit java_compilation_unit;


    public java_Type_declaration(
        String doc    ) {
        this.doc = doc;
    }


    public String getDoc() {
        return doc;
    }

    public void setDoc(String doc) {
        this.doc = doc;
    }

    public java_Compilation_unit getJava_compilation_unit() {
        return java_compilation_unit;
    }

    public void setJava_compilation_unit(java_Compilation_unit java_compilation_unit) {
        this.java_compilation_unit = java_compilation_unit;
    }

}