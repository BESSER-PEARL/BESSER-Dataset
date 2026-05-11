





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_SelectionDescription  {

    private boolean tree;
    private String message;
    private String candidatesExpression;
    private String rootExpression;
    private boolean multiple;
    private String childrenExpression;



    public viewpoint_description_SelectionDescription(
        boolean tree,        String message,        String candidatesExpression,        String rootExpression,        boolean multiple,        String childrenExpression    ) {
        this.tree = tree;
        this.message = message;
        this.candidatesExpression = candidatesExpression;
        this.rootExpression = rootExpression;
        this.multiple = multiple;
        this.childrenExpression = childrenExpression;
    }


    public boolean getTree() {
        return tree;
    }

    public void setTree(boolean tree) {
        this.tree = tree;
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
    public String getRootexpression() {
        return rootExpression;
    }

    public void setRootexpression(String rootExpression) {
        this.rootExpression = rootExpression;
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


}