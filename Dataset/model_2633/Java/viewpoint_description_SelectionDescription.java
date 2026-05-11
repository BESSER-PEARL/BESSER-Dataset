





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_SelectionDescription  {

    private boolean multiple;
    private String message;
    private String candidatesExpression;
    private String childrenExpression;
    private boolean tree;
    private String rootExpression;



    public viewpoint_description_SelectionDescription(
        boolean multiple,        String message,        String candidatesExpression,        String childrenExpression,        boolean tree,        String rootExpression    ) {
        this.multiple = multiple;
        this.message = message;
        this.candidatesExpression = candidatesExpression;
        this.childrenExpression = childrenExpression;
        this.tree = tree;
        this.rootExpression = rootExpression;
    }


    public boolean getMultiple() {
        return multiple;
    }

    public void setMultiple(boolean multiple) {
        this.multiple = multiple;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getCandidatesexpression() {
        return candidatesExpression;
    }

    public void setCandidatesexpression(String candidatesExpression) {
        this.candidatesExpression = candidatesExpression;
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