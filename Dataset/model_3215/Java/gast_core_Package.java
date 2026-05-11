





import java.util.List;
import java.util.ArrayList;

public class gast_core_Package extends NamedModelElement {

    private int linesOfCode;
    private String qualifiedName;
    private int linesOfComments;



    public gast_core_Package(
        int linesOfCode,        String qualifiedName,        int linesOfComments    ) {
        super(
        );
        this.linesOfCode = linesOfCode;
        this.qualifiedName = qualifiedName;
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
    public int getLinesofcomments() {
        return linesOfComments;
    }

    public void setLinesofcomments(int linesOfComments) {
        this.linesOfComments = linesOfComments;
    }


}