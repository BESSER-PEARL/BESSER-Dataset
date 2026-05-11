





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_SelectionDescription  {

    private String childrenExpression;
    private boolean tree;
    private boolean multiple;
    private String message;
    private String rootExpression;
    private String candidatesExpression;



    public viewpoint_description_SelectionDescription(
        String childrenExpression,        boolean tree,        boolean multiple,        String message,        String rootExpression,        String candidatesExpression    ) {
        this.childrenExpression = childrenExpression;
        this.tree = tree;
        this.multiple = multiple;
        this.message = message;
        this.rootExpression = rootExpression;
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