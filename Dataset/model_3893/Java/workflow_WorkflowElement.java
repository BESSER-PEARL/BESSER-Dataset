





import java.util.List;
import java.util.ArrayList;

public class workflow_WorkflowElement  {

    private String name;
    private int y;
    private int width;
    private String comment;
    private String workFlowElementId;
    private int height;
    private int x;



    public workflow_WorkflowElement(
        String name,        int y,        int width,        String comment,        String workFlowElementId,        int height,        int x    ) {
        this.name = name;
        this.y = y;
        this.width = width;
        this.comment = comment;
        this.workFlowElementId = workFlowElementId;
        this.height = height;
        this.x = x;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getWorkflowelementid() {
        return workFlowElementId;
    }

    public void setWorkflowelementid(String workFlowElementId) {
        this.workFlowElementId = workFlowElementId;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }


}