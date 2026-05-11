





import java.util.List;
import java.util.ArrayList;

public class gast_functions_Function extends core_SourceEntity, core_NamedModelElement {

    private int maximumNestingLevel;
    private int linesOfCode;
    private int numberOfStatements;
    private boolean operator;
    private int numberOfNodesInCFG;
    private int numberOfEdgesInCFG;
    private int linesOfComments;





    private List<GASTClass> gastclasss;




    private List<Statement> statements;




    private BlockStatement blockstatement;




    private List<Access> accesss;


    public gast_functions_Function(
        int maximumNestingLevel,        int linesOfCode,        int numberOfStatements,        boolean operator,        int numberOfNodesInCFG,        int numberOfEdgesInCFG,        int linesOfComments    ) {
        super(
        );
        this.maximumNestingLevel = maximumNestingLevel;
        this.linesOfCode = linesOfCode;
        this.numberOfStatements = numberOfStatements;
        this.operator = operator;
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.linesOfComments = linesOfComments;
        this.gastclasss = new ArrayList<>();
        this.statements = new ArrayList<>();
        this.accesss = new ArrayList<>();
    }

    public gast_functions_Function(
        int maximumNestingLevel,        int linesOfCode,        int numberOfStatements,        boolean operator,        int numberOfNodesInCFG,        int numberOfEdgesInCFG,        int linesOfComments        ArrayList<GASTClass> gastclasss,        ArrayList<Statement> statements,        ArrayList<Access> accesss    ) {
        this.maximumNestingLevel = maximumNestingLevel;
        this.linesOfCode = linesOfCode;
        this.numberOfStatements = numberOfStatements;
        this.operator = operator;
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.linesOfComments = linesOfComments;
        this.gastclasss = gastclasss;
        this.statements = statements;
        this.accesss = accesss;
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
    public int getNumberofstatements() {
        return numberOfStatements;
    }

    public void setNumberofstatements(int numberOfStatements) {
        this.numberOfStatements = numberOfStatements;
    }
    public boolean getOperator() {
        return operator;
    }

    public void setOperator(boolean operator) {
        this.operator = operator;
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
    public int getLinesofcomments() {
        return linesOfComments;
    }

    public void setLinesofcomments(int linesOfComments) {
        this.linesOfComments = linesOfComments;
    }

    public List<GASTClass> getGastclasss() {
        return gastclasss;
    }

    public void addGastclass(Gastclass gastclass) {
        this.gastclasss.add(gastclass);
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
    public List<Access> getAccesss() {
        return accesss;
    }

    public void addAccess(Access access) {
        this.accesss.add(access);
    }

}