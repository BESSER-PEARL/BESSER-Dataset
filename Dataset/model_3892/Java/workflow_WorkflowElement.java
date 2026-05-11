





import java.util.List;
import java.util.ArrayList;

public class workflow_WorkflowElement  {

    private String comment;
    private int height;
    private String id;
    private String name;
    private int width;
    private int x;
    private int y;



    public workflow_WorkflowElement(
        String comment,        int height,        String id,        String name,        int width,        int x,        int y    ) {
        this.comment = comment;
        this.height = height;
        this.id = id;
        this.name = name;
        this.width = width;
        this.x = x;
        this.y = y;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }


}