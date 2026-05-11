





import java.util.List;
import java.util.ArrayList;

public class pascal_for_statement extends repetitive_statement {

    private String name;





    private pascal_statement pascal_statement;


    public pascal_for_statement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_statement getPascal_statement() {
        return pascal_statement;
    }

    public void setPascal_statement(pascal_statement pascal_statement) {
        this.pascal_statement = pascal_statement;
    }

}