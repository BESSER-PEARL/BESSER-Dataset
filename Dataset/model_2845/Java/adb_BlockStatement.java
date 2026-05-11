





import java.util.List;
import java.util.ArrayList;

public class adb_BlockStatement extends DeclarativeBlock, CompoundStatement {

    private String blockStatementIdentifier;



    public adb_BlockStatement(
        String blockStatementIdentifier    ) {
        super(
        );
        this.blockStatementIdentifier = blockStatementIdentifier;
    }


    public String getBlockstatementidentifier() {
        return blockStatementIdentifier;
    }

    public void setBlockstatementidentifier(String blockStatementIdentifier) {
        this.blockStatementIdentifier = blockStatementIdentifier;
    }


}