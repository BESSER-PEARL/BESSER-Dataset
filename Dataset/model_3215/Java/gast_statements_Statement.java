





import java.util.List;
import java.util.ArrayList;

public class gast_statements_Statement extends SourceEntity {

    private int numberOfNodesInCFG;
    private int numberOfStatements;
    private int numberOfComments;
    private int linesOfCode;
    private int numberOfEdgesInCFG;
    private int maximumNestingLevel;





    private Statement statement;




    private BlockStatement blockstatement;


    public gast_statements_Statement(
        int numberOfNodesInCFG,        int numberOfStatements,        int numberOfComments,        int linesOfCode,        int numberOfEdgesInCFG,        int maximumNestingLevel    ) {
        super(
        );
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.numberOfStatements = numberOfStatements;
        this.numberOfComments = numberOfComments;
        this.linesOfCode = linesOfCode;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.maximumNestingLevel = maximumNestingLevel;
    }


    public int getNumberofnodesincfg() {
        return numberOfNodesInCFG;
    }

    public void setNumberofnodesincfg(int numberOfNodesInCFG) {
        this.numberOfNodesInCFG = numberOfNodesInCFG;
    }
    public int getNumberofstatements() {
        return numberOfStatements;
    }

    public void setNumberofstatements(int numberOfStatements) {
        this.numberOfStatements = numberOfStatements;
    }
    public int getNumberofcomments() {
        return numberOfComments;
    }

    public void setNumberofcomments(int numberOfComments) {
        this.numberOfComments = numberOfComments;
    }
    public int getLinesofcode() {
        return linesOfCode;
    }

    public void setLinesofcode(int linesOfCode) {
        this.linesOfCode = linesOfCode;
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

    public Statement getStatement() {
        return statement;
    }

    public void setStatement(Statement statement) {
        this.statement = statement;
    }
    public BlockStatement getBlockstatement() {
        return blockstatement;
    }

    public void setBlockstatement(BlockStatement blockstatement) {
        this.blockstatement = blockstatement;
    }

}