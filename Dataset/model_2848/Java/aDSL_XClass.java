





import java.util.List;
import java.util.ArrayList;

public class aDSL_XClass extends VarDef {

    private String name;





    private aDSL_Program adsl_program;




    private aDSL_XClass adsl_xclass;


    public aDSL_XClass(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public aDSL_Program getAdsl_program() {
        return adsl_program;
    }

    public void setAdsl_program(aDSL_Program adsl_program) {
        this.adsl_program = adsl_program;
    }
    public aDSL_XClass getAdsl_xclass() {
        return adsl_xclass;
    }

    public void setAdsl_xclass(aDSL_XClass adsl_xclass) {
        this.adsl_xclass = adsl_xclass;
    }

}