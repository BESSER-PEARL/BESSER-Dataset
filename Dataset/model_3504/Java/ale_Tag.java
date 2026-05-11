





import java.util.List;
import java.util.ArrayList;

public class ale_Tag  {

    private String name;





    private ale_Operation ale_operation;


    public ale_Tag(
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

}