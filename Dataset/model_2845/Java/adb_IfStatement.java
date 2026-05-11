





import java.util.List;
import java.util.ArrayList;

public class adb_IfStatement extends CompoundStatement {






    private adb_SequenceOfStatements adb_sequenceofstatements;




    private adb_Expression adb_expression;




    private List<adb_Expression> adb_expressions;




    private List<adb_SequenceOfStatements> adb_sequenceofstatementss;




    private adb_SequenceOfStatements adb_sequenceofstatements;


    public adb_IfStatement(
    ) {
        super(
        );
        this.adb_expressions = new ArrayList<>();
        this.adb_sequenceofstatementss = new ArrayList<>();
    }

    public adb_IfStatement(
        ArrayList<adb_Expression> adb_expressions,        ArrayList<adb_SequenceOfStatements> adb_sequenceofstatementss    ) {
        this.adb_expressions = adb_expressions;
        this.adb_sequenceofstatementss = adb_sequenceofstatementss;
    }


    public adb_SequenceOfStatements getAdb_sequenceofstatements() {
        return adb_sequenceofstatements;
    }

    public void setAdb_sequenceofstatements(adb_SequenceOfStatements adb_sequenceofstatements) {
        this.adb_sequenceofstatements = adb_sequenceofstatements;
    }
    public adb_Expression getAdb_expression() {
        return adb_expression;
    }

    public void setAdb_expression(adb_Expression adb_expression) {
        this.adb_expression = adb_expression;
    }
    public List<adb_Expression> getAdb_expressions() {
        return adb_expressions;
    }

    public void addAdb_expression(Adb_expression adb_expression) {
        this.adb_expressions.add(adb_expression);
    }
    public List<adb_SequenceOfStatements> getAdb_sequenceofstatementss() {
        return adb_sequenceofstatementss;
    }

    public void addAdb_sequenceofstatements(Adb_sequenceofstatements adb_sequenceofstatements) {
        this.adb_sequenceofstatementss.add(adb_sequenceofstatements);
    }
    public adb_SequenceOfStatements getAdb_sequenceofstatements() {
        return adb_sequenceofstatements;
    }

    public void setAdb_sequenceofstatements(adb_SequenceOfStatements adb_sequenceofstatements) {
        this.adb_sequenceofstatements = adb_sequenceofstatements;
    }

}