





import java.util.List;
import java.util.ArrayList;

public class gast_statements_Statement extends SourceEntity {

    private int numberOfNodesInCFG;
    private int maximumNestingLevel;
    private int numberOfComments;
    private int linesOfCode;
    private int numberOfStatements;
    private int numberOfEdgesInCFG;





    private Statement statement;




    private BlockStatement blockstatement;


    public gast_statements_Statement(
        int numberOfNodesInCFG,        int maximumNestingLevel,        int numberOfComments,        int linesOfCode,        int numberOfStatements,        int numberOfEdgesInCFG    ) {
        super(
        );
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.maximumNestingLevel = maximumNestingLevel;
        this.numberOfComments = numberOfComments;
        this.linesOfCode = linesOfCode;
        this.numberOfStatements = numberOfStatements;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
    }


    public int getNumberofnodesincfg() {
        return numberOfNodesInCFG;
    }

    public void setNumberofnodesincfg(int numberOfNodesInCFG) {
        this.numberOfNodesInCFG = numberOfNodesInCFG;
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
    public int getNumberofedgesincfg() {
        return numberOfEdgesInCFG;
    }

    public void setNumberofedgesincfg(int numberOfEdgesInCFG) {
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
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