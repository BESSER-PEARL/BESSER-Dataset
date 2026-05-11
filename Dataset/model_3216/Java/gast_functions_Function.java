





import java.util.List;
import java.util.ArrayList;

public class gast_functions_Function extends core_NamedModelElement, core_SourceEntity {

    private int linesOfComments;
    private int maximumNestingLevel;
    private int numberOfStatements;
    private int linesOfCode;
    private int numberOfNodesInCFG;
    private int numberOfEdgesInCFG;
    private boolean operator;





    private BlockStatement blockstatement;




    private List<Statement> statements;


    public gast_functions_Function(
        int linesOfComments,        int maximumNestingLevel,        int numberOfStatements,        int linesOfCode,        int numberOfNodesInCFG,        int numberOfEdgesInCFG,        boolean operator    ) {
        super(
        );
        this.linesOfComments = linesOfComments;
        this.maximumNestingLevel = maximumNestingLevel;
        this.numberOfStatements = numberOfStatements;
        this.linesOfCode = linesOfCode;
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.operator = operator;
        this.statements = new ArrayList<>();
    }

    public gast_functions_Function(
        int linesOfComments,        int maximumNestingLevel,        int numberOfStatements,        int linesOfCode,        int numberOfNodesInCFG,        int numberOfEdgesInCFG,        boolean operator        ArrayList<Statement> statements    ) {
        this.linesOfComments = linesOfComments;
        this.maximumNestingLevel = maximumNestingLevel;
        this.numberOfStatements = numberOfStatements;
        this.linesOfCode = linesOfCode;
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.operator = operator;
        this.statements = statements;
    }

    public int getLinesofcomments() {
        return linesOfComments;
    }

    public void setLinesofcomments(int linesOfComments) {
        this.linesOfComments = linesOfComments;
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
    public boolean getOperator() {
        return operator;
    }

    public void setOperator(boolean operator) {
        this.operator = operator;
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

}