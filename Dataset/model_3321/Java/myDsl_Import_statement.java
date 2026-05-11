





import java.util.List;
import java.util.ArrayList;

public class myDsl_Import_statement  {

    private String pacName;
    private String className;





    private myDsl_Compilation_unit mydsl_compilation_unit;


    public myDsl_Import_statement(
        String pacName,        String className    ) {
        this.pacName = pacName;
        this.className = className;
    }


    public String getPacname() {
        return pacName;
    }

    public void setPacname(String pacName) {
        this.pacName = pacName;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }

    public myDsl_Compilation_unit getMydsl_compilation_unit() {
        return mydsl_compilation_unit;
    }

    public void setMydsl_compilation_unit(myDsl_Compilation_unit mydsl_compilation_unit) {
        this.mydsl_compilation_unit = mydsl_compilation_unit;
    }

}