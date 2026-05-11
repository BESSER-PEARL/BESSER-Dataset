





import java.util.List;
import java.util.ArrayList;

public class gast_statements_Statement extends SourceEntity {

    private int numberOfComments;
    private int numberOfNodesInCFG;
    private int numberOfEdgesInCFG;
    private int maximumNestingLevel;
    private int numberOfStatements;
    private int linesOfCode;





    private List<Statement> statements;




    private BlockStatement blockstatement;




    private List<Statement> statements;




    private Statement statement;


    public gast_statements_Statement(
        int numberOfComments,        int numberOfNodesInCFG,        int numberOfEdgesInCFG,        int maximumNestingLevel,        int numberOfStatements,        int linesOfCode    ) {
        super(
        );
        this.numberOfComments = numberOfComments;
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.maximumNestingLevel = maximumNestingLevel;
        this.numberOfStatements = numberOfStatements;
        this.linesOfCode = linesOfCode;
        this.statements = new ArrayList<>();
        this.statements = new ArrayList<>();
    }

    public gast_statements_Statement(
        int numberOfComments,        int numberOfNodesInCFG,        int numberOfEdgesInCFG,        int maximumNestingLevel,        int numberOfStatements,        int linesOfCode        ArrayList<Statement> statements,        ArrayList<Statement> statements    ) {
        this.numberOfComments = numberOfComments;
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.maximumNestingLevel = maximumNestingLevel;
        this.numberOfStatements = numberOfStatements;
        this.linesOfCode = linesOfCode;
        this.statements = statements;
        this.statements = statements;
    }

    public int getNumberofcomments() {
        return numberOfComments;
    }

    public void setNumberofcomments(int numberOfComments) {
        this.numberOfComments = numberOfComments;
    }
    public int getNumberofnodesincfg() {
        return numberOfNodesInCFG;
    }

    public void setNumberofnodesincfg(int numberOfNodesInCFG) {
        this.numberOfNodesInCFG = numberOfNodesInCFG;
    }
    public int getNumberofedgesincfg() {
        return numberOfEdgesInCFG;
    }

    public void setNumberofedgesincfg(int numberOfEdgesInCFG) {
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
    }
    public int getMaximumnestinglevel() {
        return maximumNestingLevel;
    }

    public void setMaximumnestinglevel(int maximumNestingLevel) {
        this.maximumNestingLevel = maximumNestingLevel;
    }
    public int getNumberofstatements() {
        return numberOfStatements;
    }

    public void setNumberofstatements(int numberOfStatements) {
        this.numberOfStatements = numberOfStatements;
    }
    public int getLinesofcode() {
        return linesOfCode;
    }

    public void setLinesofcode(int linesOfCode) {
        this.linesOfCode = linesOfCode;
    }

    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }
    public BlockStatement getBlockstatement() {
        return blockstatement;
    }

    public void setBlockstatement(BlockStatement blockstatement) {
        this.blockstatement = blockstatement;
    }
    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }
    public Statement getStatement() {
        return statement;
    }

    public void setStatement(Statement statement) {
        this.statement = statement;
    }

}