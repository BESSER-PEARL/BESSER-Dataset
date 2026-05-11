





import java.util.List;
import java.util.ArrayList;

public class gast_core_Package extends NamedModelElement {

    private int linesOfComments;
    private int linesOfCode;
    private String qualifiedName;





    private Root root;


    public gast_core_Package(
        int linesOfComments,        int linesOfCode,        String qualifiedName    ) {
        super(
        );
        this.linesOfComments = linesOfComments;
        this.linesOfCode = linesOfCode;
        this.qualifiedName = qualifiedName;
    }


    public int getLinesofcomments() {
        return linesOfComments;
    }

    public void setLinesofcomments(int linesOfComments) {
        this.linesOfComments = linesOfComments;
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

    public Root getRoot() {
        return root;
    }

    public void setRoot(Root root) {
        this.root = root;
    }

}