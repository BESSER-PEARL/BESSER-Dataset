





import java.util.List;
import java.util.ArrayList;

public class pascal_variable  {

    private String name;





    private pascal_assignment_statement pascal_assignment_statement;


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

    public pascal_assignment_statement getPascal_assignment_statement() {
        return pascal_assignment_statement;
    }

    public void setPascal_assignment_statement(pascal_assignment_statement pascal_assignment_statement) {
        this.pascal_assignment_statement = pascal_assignment_statement;
    }

}