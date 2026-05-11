





import java.util.List;
import java.util.ArrayList;

public class while_Val extends Exp {

    private String id;





    private while_Program while_program;


    public while_Val(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public while_Program getWhile_program() {
        return while_program;
    }

    public void setWhile_program(while_Program while_program) {
        this.while_program = while_program;
    }

}