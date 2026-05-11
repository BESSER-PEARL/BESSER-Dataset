





import java.util.List;
import java.util.ArrayList;

public class gast_core_Package extends NamedModelElement {

    private String qualifiedName;
    private int linesOfCode;
    private int linesOfComments;





    private Root root;




    private List<GlobalFunction> globalfunctions;


    public gast_core_Package(
        String qualifiedName,        int linesOfCode,        int linesOfComments    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
        this.linesOfCode = linesOfCode;
        this.linesOfComments = linesOfComments;
        this.globalfunctions = new ArrayList<>();
    }

    public gast_core_Package(
        String qualifiedName,        int linesOfCode,        int linesOfComments        ArrayList<GlobalFunction> globalfunctions    ) {
        this.qualifiedName = qualifiedName;
        this.linesOfCode = linesOfCode;
        this.linesOfComments = linesOfComments;
        this.globalfunctions = globalfunctions;
    }

    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }
    public int getLinesofcode() {
        return linesOfCode;
    }

    public void setLinesofcode(int linesOfCode) {
        this.linesOfCode = linesOfCode;
    }
    public int getLinesofcomments() {
        return linesOfComments;
    }

    public void setLinesofcomments(int linesOfComments) {
        this.linesOfComments = linesOfComments;
    }

    public Root getRoot() {
        return root;
    }

    public void setRoot(Root root) {
        this.root = root;
    }
    public List<GlobalFunction> getGlobalfunctions() {
        return globalfunctions;
    }

    public void addGlobalfunction(Globalfunction globalfunction) {
        this.globalfunctions.add(globalfunction);
    }

}