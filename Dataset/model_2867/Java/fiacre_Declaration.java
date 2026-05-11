





import java.util.List;
import java.util.ArrayList;

public class fiacre_Declaration  {

    private String name;





    private fiacre_Program fiacre_program;


    public fiacre_Declaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fiacre_Program getFiacre_program() {
        return fiacre_program;
    }

    public void setFiacre_program(fiacre_Program fiacre_program) {
        this.fiacre_program = fiacre_program;
    }

}