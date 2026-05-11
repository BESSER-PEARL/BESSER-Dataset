





import java.util.List;
import java.util.ArrayList;

public class model_Comment extends Node {

    private int height;
    private int width;
    private String content;





    private model_Diagram model_diagram;


    public model_Comment(
        int height,        int width,        String content    ) {
        super(
        );
        this.height = height;
        this.width = width;
        this.content = content;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public model_Diagram getModel_diagram() {
        return model_diagram;
    }

    public void setModel_diagram(model_Diagram model_diagram) {
        this.model_diagram = model_diagram;
    }

}