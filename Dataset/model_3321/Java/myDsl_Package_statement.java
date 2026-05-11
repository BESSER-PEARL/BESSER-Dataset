





import java.util.List;
import java.util.ArrayList;

public class myDsl_Package_statement  {

    private String pacName;





    private myDsl_Compilation_unit mydsl_compilation_unit;


    public myDsl_Package_statement(
        String pacName    ) {
        this.pacName = pacName;
    }


    public String getPacname() {
        return pacName;
    }

    public void setPacname(String pacName) {
        this.pacName = pacName;
    }

    public myDsl_Compilation_unit getMydsl_compilation_unit() {
        return mydsl_compilation_unit;
    }

    public void setMydsl_compilation_unit(myDsl_Compilation_unit mydsl_compilation_unit) {
        this.mydsl_compilation_unit = mydsl_compilation_unit;
    }

}