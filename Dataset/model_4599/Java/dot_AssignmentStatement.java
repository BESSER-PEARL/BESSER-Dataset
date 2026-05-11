





import java.util.List;
import java.util.ArrayList;

public class dot_AssignmentStatement extends Commentable, Statement {

    private String left;
    private String right;



    public dot_AssignmentStatement(
        String left,        String right    ) {
        super(
        );
        this.left = left;
        this.right = right;
    }


    public String getLeft() {
        return left;
    }

    public void setLeft(String left) {
        this.left = left;
    }
    public String getRight() {
        return right;
    }

    public void setRight(String right) {
        this.right = right;
    }


}