





import java.util.List;
import java.util.ArrayList;

public class unql_Definition  {

    private String name;
    private String type;





    private unql_Program unql_program;


    public unql_Definition(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public unql_Program getUnql_program() {
        return unql_program;
    }

    public void setUnql_program(unql_Program unql_program) {
        this.unql_program = unql_program;
    }

}