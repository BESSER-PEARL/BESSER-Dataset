





import java.util.List;
import java.util.ArrayList;

public class paplj_Type  {

    private String name;





    private paplj_Type paplj_type;




    private paplj_Program paplj_program;


    public paplj_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public paplj_Type getPaplj_type() {
        return paplj_type;
    }

    public void setPaplj_type(paplj_Type paplj_type) {
        this.paplj_type = paplj_type;
    }
    public paplj_Program getPaplj_program() {
        return paplj_program;
    }

    public void setPaplj_program(paplj_Program paplj_program) {
        this.paplj_program = paplj_program;
    }

}