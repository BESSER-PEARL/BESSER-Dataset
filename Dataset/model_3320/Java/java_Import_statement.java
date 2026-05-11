





import java.util.List;
import java.util.ArrayList;

public class java_Import_statement  {

    private String classname;
    private String packagename;





    private java_Compilation_unit java_compilation_unit;


    public java_Import_statement(
        String classname,        String packagename    ) {
        this.classname = classname;
        this.packagename = packagename;
    }


    public String getClassname() {
        return classname;
    }

    public void setClassname(String classname) {
        this.classname = classname;
    }
    public String getPackagename() {
        return packagename;
    }

    public void setPackagename(String packagename) {
        this.packagename = packagename;
    }

    public java_Compilation_unit getJava_compilation_unit() {
        return java_compilation_unit;
    }

    public void setJava_compilation_unit(java_Compilation_unit java_compilation_unit) {
        this.java_compilation_unit = java_compilation_unit;
    }

}