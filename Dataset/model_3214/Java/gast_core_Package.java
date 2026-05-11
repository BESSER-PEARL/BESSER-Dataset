





import java.util.List;
import java.util.ArrayList;

public class gast_core_Package extends NamedModelElement {

    private int linesOfCode;
    private String qualifiedName;
    private int linesOfComments;





    private Root root;




    private List<GlobalFunction> globalfunctions;


    public gast_core_Package(
        int linesOfCode,        String qualifiedName,        int linesOfComments    ) {
        super(
        );
        this.linesOfCode = linesOfCode;
        this.qualifiedName = qualifiedName;
        this.linesOfComments = linesOfComments;
        this.globalfunctions = new ArrayList<>();
    }

    public gast_core_Package(
        int linesOfCode,        String qualifiedName,        int linesOfComments        ArrayList<GlobalFunction> globalfunctions    ) {
        this.linesOfCode = linesOfCode;
        this.qualifiedName = qualifiedName;
        this.linesOfComments = linesOfComments;
        this.globalfunctions = globalfunctions;
    }

    public int getLinesofcode() {
        return linesOfCode;
    }

    public void setLinesofcode(int linesOfCode) {
        this.linesOfCode = linesOfCode;
    }
    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
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