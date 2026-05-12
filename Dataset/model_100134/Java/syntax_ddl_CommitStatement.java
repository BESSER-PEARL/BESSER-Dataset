





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_CommitStatement extends DefinitionStatement {

    private boolean hold;



    public syntax_ddl_CommitStatement(
        boolean hold    ) {
        super(
        );
        this.hold = hold;
    }


    public boolean getHold() {
        return hold;
    }

    public void setHold(boolean hold) {
        this.hold = hold;
    }


}