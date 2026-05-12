





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_CreateIndexStatement extends DefinitionStatement {

    private boolean unique;



    public syntax_ddl_CreateIndexStatement(
        boolean unique    ) {
        super(
        );
        this.unique = unique;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }


}