





import java.util.List;
import java.util.ArrayList;

public class gast_statements_Statement extends SourceEntity {

    private int maximumNestingLevel;
    private int numberOfComments;
    private int numberOfEdgesInCFG;
    private int linesOfCode;
    private int numberOfStatements;
    private int numberOfNodesInCFG;





    private List<Statement> statements;




    private CloneInstance cloneinstance;




    private Branch branch;




    private Statement statement;




    private List<Statement> statements;




    private BlockStatement blockstatement;




    private LoopStatement loopstatement;


    public gast_statements_Statement(
        int maximumNestingLevel,        int numberOfComments,        int numberOfEdgesInCFG,        int linesOfCode,        int numberOfStatements,        int numberOfNodesInCFG    ) {
        super(
        );
        this.maximumNestingLevel = maximumNestingLevel;
        this.numberOfComments = numberOfComments;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.linesOfCode = linesOfCode;
        this.numberOfStatements = numberOfStatements;
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.statements = new ArrayList<>();
        this.statements = new ArrayList<>();
    }

    public gast_statements_Statement(
        int maximumNestingLevel,        int numberOfComments,        int numberOfEdgesInCFG,        int linesOfCode,        int numberOfStatements,        int numberOfNodesInCFG        ArrayList<Statement> statements,        ArrayList<Statement> statements    ) {
        this.maximumNestingLevel = maximumNestingLevel;
        this.numberOfComments = numberOfComments;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.linesOfCode = linesOfCode;
        this.numberOfStatements = numberOfStatements;
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.statements = statements;
        this.statements = statements;
    }

    public int getMaximumnestinglevel() {
        return maximumNestingLevel;
    }

    public void setMaximumnestinglevel(int maximumNestingLevel) {
        this.maximumNestingLevel = maximumNestingLevel;
    }
    public int getNumberofcomments() {
        return numberOfComments;
    }

    public void setNumberofcomments(int numberOfComments) {
        this.numberOfComments = numberOfComments;
    }
    public int getNumberofedgesincfg() {
        return numberOfEdgesInCFG;
    }

    public void setNumberofedgesincfg(int numberOfEdgesInCFG) {
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
    }
    public int getLinesofcode() {
        return linesOfCode;
    }

    public void setLinesofcode(int linesOfCode) {
        this.linesOfCode = linesOfCode;
    }
    public int getNumberofstatements() {
        return numberOfStatements;
    }

    public void setNumberofstatements(int numberOfStatements) {
        this.numberOfStatements = numberOfStatements;
    }
    public int getNumberofnodesincfg() {
        return numberOfNodesInCFG;
    }

    public void setNumberofnodesincfg(int numberOfNodesInCFG) {
        this.numberOfNodesInCFG = numberOfNodesInCFG;
    }

    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }
    public CloneInstance getCloneinstance() {
        return cloneinstance;
    }

    public void setCloneinstance(CloneInstance cloneinstance) {
        this.cloneinstance = cloneinstance;
    }
    public Branch getBranch() {
        return branch;
    }

    public void setBranch(Branch branch) {
        this.branch = branch;
    }
    public Statement getStatement() {
        return statement;
    }

    public void setStatement(Statement statement) {
        this.statement = statement;
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
    public LoopStatement getLoopstatement() {
        return loopstatement;
    }

    public void setLoopstatement(LoopStatement loopstatement) {
        this.loopstatement = loopstatement;
    }

}