





import java.util.List;
import java.util.ArrayList;

public class ale_rType  {

    private String name;





    private ale_Operation ale_operation;




    private ale_Attribute ale_attribute;


    public ale_rType(
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
    public ale_Attribute getAle_attribute() {
        return ale_attribute;
    }

    public void setAle_attribute(ale_Attribute ale_attribute) {
        this.ale_attribute = ale_attribute;
    }

}