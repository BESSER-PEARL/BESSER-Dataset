





import java.util.List;
import java.util.ArrayList;

public class adb_ExtendedReturnStatement extends CompoundStatement {

    private String identifier;





    private adb_Expression adb_expression;




    private adb_HandledSequenceOfStatements adb_handledsequenceofstatements;


    public adb_ExtendedReturnStatement(
        String identifier    ) {
        super(
        );
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public adb_Expression getAdb_expression() {
        return adb_expression;
    }

    public void setAdb_expression(adb_Expression adb_expression) {
        this.adb_expression = adb_expression;
    }
    public adb_HandledSequenceOfStatements getAdb_handledsequenceofstatements() {
        return adb_handledsequenceofstatements;
    }

    public void setAdb_handledsequenceofstatements(adb_HandledSequenceOfStatements adb_handledsequenceofstatements) {
        this.adb_handledsequenceofstatements = adb_handledsequenceofstatements;
    }

}