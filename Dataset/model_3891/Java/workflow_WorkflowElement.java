





import java.util.List;
import java.util.ArrayList;

public class workflow_WorkflowElement  {

    private int width;
    private String id;
    private String comment;
    private int y;
    private int x;
    private int height;
    private String name;



    public workflow_WorkflowElement(
        int width,        String id,        String comment,        int y,        int x,        int height,        String name    ) {
        this.width = width;
        this.id = id;
        this.comment = comment;
        this.y = y;
        this.x = x;
        this.height = height;
        this.name = name;
    }


    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}