





import java.util.List;
import java.util.ArrayList;

public class gast_functions_Function extends core_NamedModelElement, core_SourceEntity {

    private boolean operator;
    private int numberOfStatements;
    private int linesOfComments;
    private int numberOfNodesInCFG;
    private int linesOfCode;
    private int numberOfEdgesInCFG;
    private int maximumNestingLevel;





    private List<Statement> statements;




    private List<Access> accesss;




    private List<GASTClass> gastclasss;




    private BlockStatement blockstatement;


    public gast_functions_Function(
        boolean operator,        int numberOfStatements,        int linesOfComments,        int numberOfNodesInCFG,        int linesOfCode,        int numberOfEdgesInCFG,        int maximumNestingLevel    ) {
        super(
        );
        this.operator = operator;
        this.numberOfStatements = numberOfStatements;
        this.linesOfComments = linesOfComments;
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.linesOfCode = linesOfCode;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.maximumNestingLevel = maximumNestingLevel;
        this.statements = new ArrayList<>();
        this.accesss = new ArrayList<>();
        this.gastclasss = new ArrayList<>();
    }

    public gast_functions_Function(
        boolean operator,        int numberOfStatements,        int linesOfComments,        int numberOfNodesInCFG,        int linesOfCode,        int numberOfEdgesInCFG,        int maximumNestingLevel        ArrayList<Statement> statements,        ArrayList<Access> accesss,        ArrayList<GASTClass> gastclasss    ) {
        this.operator = operator;
        this.numberOfStatements = numberOfStatements;
        this.linesOfComments = linesOfComments;
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.linesOfCode = linesOfCode;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.maximumNestingLevel = maximumNestingLevel;
        this.statements = statements;
        this.accesss = accesss;
        this.gastclasss = gastclasss;
    }

    public boolean getOperator() {
        return operator;
    }

    public void setOperator(boolean operator) {
        this.operator = operator;
    }
    public int getNumberofstatements() {
        return numberOfStatements;
    }

    public void setNumberofstatements(int numberOfStatements) {
        this.numberOfStatements = numberOfStatements;
    }
    public int getLinesofcomments() {
        return linesOfComments;
    }

    public void setLinesofcomments(int linesOfComments) {
        this.linesOfComments = linesOfComments;
    }
    public int getNumberofnodesincfg() {
        return numberOfNodesInCFG;
    }

    public void setNumberofnodesincfg(int numberOfNodesInCFG) {
        this.numberOfNodesInCFG = numberOfNodesInCFG;
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

    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }
    public List<Access> getAccesss() {
        return accesss;
    }

    public void addAccess(Access access) {
        this.accesss.add(access);
    }
    public List<GASTClass> getGastclasss() {
        return gastclasss;
    }

    public void addGastclass(Gastclass gastclass) {
        this.gastclasss.add(gastclass);
    }
    public BlockStatement getBlockstatement() {
        return blockstatement;
    }

    public void setBlockstatement(BlockStatement blockstatement) {
        this.blockstatement = blockstatement;
    }

}