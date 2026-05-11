





import java.util.List;
import java.util.ArrayList;

public class types_Property  {

    private String name;





    private types_Operation types_operation;


    public types_Property(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public types_Operation getTypes_operation() {
        return types_operation;
    }

    public void setTypes_operation(types_Operation types_operation) {
        this.types_operation = types_operation;
    }

}