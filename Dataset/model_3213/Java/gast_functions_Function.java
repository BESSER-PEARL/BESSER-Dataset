





import java.util.List;
import java.util.ArrayList;

public class gast_functions_Function extends core_NamedModelElement, core_SourceEntity {

    private int numberOfNodesInCFG;
    private int linesOfCode;
    private int numberOfEdgesInCFG;
    private int maximumNestingLevel;
    private int numberOfStatements;
    private int linesOfComments;
    private boolean operator;





    private List<GASTClass> gastclasss;




    private List<Statement> statements;




    private List<Access> accesss;




    private BlockStatement blockstatement;


    public gast_functions_Function(
        int numberOfNodesInCFG,        int linesOfCode,        int numberOfEdgesInCFG,        int maximumNestingLevel,        int numberOfStatements,        int linesOfComments,        boolean operator    ) {
        super(
        );
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.linesOfCode = linesOfCode;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.maximumNestingLevel = maximumNestingLevel;
        this.numberOfStatements = numberOfStatements;
        this.linesOfComments = linesOfComments;
        this.operator = operator;
        this.gastclasss = new ArrayList<>();
        this.statements = new ArrayList<>();
        this.accesss = new ArrayList<>();
    }

    public gast_functions_Function(
        int numberOfNodesInCFG,        int linesOfCode,        int numberOfEdgesInCFG,        int maximumNestingLevel,        int numberOfStatements,        int linesOfComments,        boolean operator        ArrayList<GASTClass> gastclasss,        ArrayList<Statement> statements,        ArrayList<Access> accesss    ) {
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.linesOfCode = linesOfCode;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.maximumNestingLevel = maximumNestingLevel;
        this.numberOfStatements = numberOfStatements;
        this.linesOfComments = linesOfComments;
        this.operator = operator;
        this.gastclasss = gastclasss;
        this.statements = statements;
        this.accesss = accesss;
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
    public boolean getOperator() {
        return operator;
    }

    public void setOperator(boolean operator) {
        this.operator = operator;
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
    public List<Access> getAccesss() {
        return accesss;
    }

    public void addAccess(Access access) {
        this.accesss.add(access);
    }
    public BlockStatement getBlockstatement() {
        return blockstatement;
    }

    public void setBlockstatement(BlockStatement blockstatement) {
        this.blockstatement = blockstatement;
    }

}