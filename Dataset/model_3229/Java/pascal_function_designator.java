





import java.util.List;
import java.util.ArrayList;

public class pascal_function_designator  {

    private String name;





    private pascal_simple_statement pascal_simple_statement;


    public pascal_function_designator(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_simple_statement getPascal_simple_statement() {
        return pascal_simple_statement;
    }

    public void setPascal_simple_statement(pascal_simple_statement pascal_simple_statement) {
        this.pascal_simple_statement = pascal_simple_statement;
    }

}