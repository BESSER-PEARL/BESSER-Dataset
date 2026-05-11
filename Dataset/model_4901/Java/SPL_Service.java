





import java.util.List;
import java.util.ArrayList;

public class SPL_Service extends LocatedElement {

    private String name;





    private SPL_Program spl_program;


    public SPL_Service(
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

    public SPL_Program getSpl_program() {
        return spl_program;
    }

    public void setSpl_program(SPL_Program spl_program) {
        this.spl_program = spl_program;
    }

}