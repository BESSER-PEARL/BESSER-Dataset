





import java.util.List;
import java.util.ArrayList;

public class gast_functions_Function extends core_NamedModelElement, core_SourceEntity {

    private boolean operator;
    private int numberOfEdgesInCFG;
    private int linesOfCode;
    private int numberOfStatements;
    private int numberOfNodesInCFG;
    private int maximumNestingLevel;
    private int linesOfComments;





    private List<GASTClass> gastclasss;




    private List<Access> accesss;


    public gast_functions_Function(
        boolean operator,        int numberOfEdgesInCFG,        int linesOfCode,        int numberOfStatements,        int numberOfNodesInCFG,        int maximumNestingLevel,        int linesOfComments    ) {
        super(
        );
        this.operator = operator;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.linesOfCode = linesOfCode;
        this.numberOfStatements = numberOfStatements;
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.maximumNestingLevel = maximumNestingLevel;
        this.linesOfComments = linesOfComments;
        this.gastclasss = new ArrayList<>();
        this.accesss = new ArrayList<>();
    }

    public gast_functions_Function(
        boolean operator,        int numberOfEdgesInCFG,        int linesOfCode,        int numberOfStatements,        int numberOfNodesInCFG,        int maximumNestingLevel,        int linesOfComments        ArrayList<GASTClass> gastclasss,        ArrayList<Access> accesss    ) {
        this.operator = operator;
        this.numberOfEdgesInCFG = numberOfEdgesInCFG;
        this.linesOfCode = linesOfCode;
        this.numberOfStatements = numberOfStatements;
        this.numberOfNodesInCFG = numberOfNodesInCFG;
        this.maximumNestingLevel = maximumNestingLevel;
        this.linesOfComments = linesOfComments;
        this.gastclasss = gastclasss;
        this.accesss = accesss;
    }

    public boolean getOperator() {
        return operator;
    }

    public void setOperator(boolean operator) {
        this.operator = operator;
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
    public int getMaximumnestinglevel() {
        return maximumNestingLevel;
    }

    public void setMaximumnestinglevel(int maximumNestingLevel) {
        this.maximumNestingLevel = maximumNestingLevel;
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
    public List<Access> getAccesss() {
        return accesss;
    }

    public void addAccess(Access access) {
        this.accesss.add(access);
    }

}