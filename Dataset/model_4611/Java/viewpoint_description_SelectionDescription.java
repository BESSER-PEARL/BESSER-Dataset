





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_SelectionDescription  {

    private boolean tree;
    private boolean multiple;
    private String childrenExpression;
    private String rootExpression;
    private String message;
    private String candidatesExpression;



    public viewpoint_description_SelectionDescription(
        boolean tree,        boolean multiple,        String childrenExpression,        String rootExpression,        String message,        String candidatesExpression    ) {
        this.tree = tree;
        this.multiple = multiple;
        this.childrenExpression = childrenExpression;
        this.rootExpression = rootExpression;
        this.message = message;
        this.candidatesExpression = candidatesExpression;
    }


    public boolean getTree() {
        return tree;
    }

    public void setTree(boolean tree) {
        this.tree = tree;
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
    public String getRootexpression() {
        return rootExpression;
    }

    public void setRootexpression(String rootExpression) {
        this.rootExpression = rootExpression;
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


}