





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_SelectionDescription  {

    private String rootExpression;
    private boolean multiple;
    private boolean tree;
    private String childrenExpression;
    private String message;
    private String candidatesExpression;



    public viewpoint_description_SelectionDescription(
        String rootExpression,        boolean multiple,        boolean tree,        String childrenExpression,        String message,        String candidatesExpression    ) {
        this.rootExpression = rootExpression;
        this.multiple = multiple;
        this.tree = tree;
        this.childrenExpression = childrenExpression;
        this.message = message;
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
    public boolean getTree() {
        return tree;
    }

    public void setTree(boolean tree) {
        this.tree = tree;
    }
    public String getChildrenexpression() {
        return childrenExpression;
    }

    public void setChildrenexpression(String childrenExpression) {
        this.childrenExpression = childrenExpression;
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