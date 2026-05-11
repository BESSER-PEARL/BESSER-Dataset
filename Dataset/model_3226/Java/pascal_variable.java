





import java.util.List;
import java.util.ArrayList;

public class pascal_variable  {

    private String name;





    private pascal_with_statement pascal_with_statement;


    public pascal_variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_with_statement getPascal_with_statement() {
        return pascal_with_statement;
    }

    public void setPascal_with_statement(pascal_with_statement pascal_with_statement) {
        this.pascal_with_statement = pascal_with_statement;
    }

}