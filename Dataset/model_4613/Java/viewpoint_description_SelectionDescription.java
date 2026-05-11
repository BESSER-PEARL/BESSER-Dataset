





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_SelectionDescription  {

    private String candidatesExpression;
    private String message;
    private boolean multiple;
    private String childrenExpression;
    private boolean tree;
    private String rootExpression;



    public viewpoint_description_SelectionDescription(
        String candidatesExpression,        String message,        boolean multiple,        String childrenExpression,        boolean tree,        String rootExpression    ) {
        this.candidatesExpression = candidatesExpression;
        this.message = message;
        this.multiple = multiple;
        this.childrenExpression = childrenExpression;
        this.tree = tree;
        this.rootExpression = rootExpression;
    }


    public String getCandidatesexpression() {
        return candidatesExpression;
    }

    public void setCandidatesexpression(String candidatesExpression) {
        this.candidatesExpression = candidatesExpression;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public boolean getMultiple() {
        return multiple;
    }

    public void setMultiple(boolean multiple) {
        this.multiple = multiple;
    }
    public String getChildrenexpression() {
        return childrenExpression;
    }

    public void setChildrenexpression(String childrenExpression) {
        this.childrenExpression = childrenExpression;
    }
    public boolean getTree() {
        return tree;
    }

    public void setTree(boolean tree) {
        this.tree = tree;
    }
    public String getRootexpression() {
        return rootExpression;
    }

    public void setRootexpression(String rootExpression) {
        this.rootExpression = rootExpression;
    }


}