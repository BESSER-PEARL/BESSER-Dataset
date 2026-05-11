





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_SelectionDescription  {

    private String message;
    private boolean tree;
    private boolean multiple;
    private String childrenExpression;
    private String rootExpression;
    private String candidatesExpression;



    public viewpoint_description_SelectionDescription(
        String message,        boolean tree,        boolean multiple,        String childrenExpression,        String rootExpression,        String candidatesExpression    ) {
        this.message = message;
        this.tree = tree;
        this.multiple = multiple;
        this.childrenExpression = childrenExpression;
        this.rootExpression = rootExpression;
        this.candidatesExpression = candidatesExpression;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
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
    public String getCandidatesexpression() {
        return candidatesExpression;
    }

    public void setCandidatesexpression(String candidatesExpression) {
        this.candidatesExpression = candidatesExpression;
    }


}