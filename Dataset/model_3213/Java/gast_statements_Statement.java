





import java.util.List;
import java.util.ArrayList;

public class gast_statements_Statement extends SourceEntity {

    private int maximumNestingLevel;
    private int linesOfCode;
    private int numberOfNodesInCFG;
    private int numberOfComments;
    private int numberOfStatements;
    private int numberOfEdgesInCFG;





    private BlockStatement blockstatement;




    private Statement statement;




    private Branch branch;


    public gast_statements_Statement(
        int maximumNestingLevel,        int linesOfCode,        int numberOfNodesInCFG,        int numberOfComments,        int numberOfStatements,        int numberOfEdgesInCFG    ) {
        super(
        );
        this.maximumNestingLevel = maximumNestingLevel;
        this.linesOfCode = linesOfCode;
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.numberOfComments = numberOfComments;
        this.numberOfStatements = numberOfStatements;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
    }


    public int getMaximumnestinglevel() {
        return maximumNestingLevel;
    }

    public void setMaximumnestinglevel(int maximumNestingLevel) {
        this.maximumNestingLevel = maximumNestingLevel;
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
    public int getNumberofcomments() {
        return numberOfComments;
    }

    public void setNumberofcomments(int numberOfComments) {
        this.numberOfComments = numberOfComments;
    }
    public int getNumberofstatements() {
        return numberOfStatements;
    }

    public void setNumberofstatements(int numberOfStatements) {
        this.numberOfStatements = numberOfStatements;
    }
    public int getNumberofedgesincfg() {
        return numberOfEdgesInCFG;
    }

    public void setNumberofedgesincfg(int numberOfEdgesInCFG) {
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
    }

    public BlockStatement getBlockstatement() {
        return blockstatement;
    }

    public void setBlockstatement(BlockStatement blockstatement) {
        this.blockstatement = blockstatement;
    }
    public Statement getStatement() {
        return statement;
    }

    public void setStatement(Statement statement) {
        this.statement = statement;
    }
    public Branch getBranch() {
        return branch;
    }

    public void setBranch(Branch branch) {
        this.branch = branch;
    }

}