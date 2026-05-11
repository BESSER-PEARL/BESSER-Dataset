





import java.util.List;
import java.util.ArrayList;

public class gv_AssignmentStatement extends Statement, Commentable {

    private String right;
    private String left;



    public gv_AssignmentStatement(
        String right,        String left    ) {
        super(
        );
        this.right = right;
        this.left = left;
    }


    public String getRight() {
        return right;
    }

    public void setRight(String right) {
        this.right = right;
    }
    public String getLeft() {
        return left;
    }

    public void setLeft(String left) {
        this.left = left;
    }


}