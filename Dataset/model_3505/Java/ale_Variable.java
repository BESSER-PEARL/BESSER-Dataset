





import java.util.List;
import java.util.ArrayList;

public class ale_Variable  {

    private String name;





    private ale_Operation ale_operation;




    private ale_rType ale_rtype;


    public ale_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ale_Operation getAle_operation() {
        return ale_operation;
    }

    public void setAle_operation(ale_Operation ale_operation) {
        this.ale_operation = ale_operation;
    }
    public ale_rType getAle_rtype() {
        return ale_rtype;
    }

    public void setAle_rtype(ale_rType ale_rtype) {
        this.ale_rtype = ale_rtype;
    }

}