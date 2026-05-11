





import java.util.List;
import java.util.ArrayList;

public class model_Bounds  {

    private int height;
    private int x;
    private int width;
    private int y;





    private model_DiagramModelObject model_diagrammodelobject;


    public model_Bounds(
        int height,        int x,        int width,        int y    ) {
        this.height = height;
        this.x = x;
        this.width = width;
        this.y = y;
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
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public model_DiagramModelObject getModel_diagrammodelobject() {
        return model_diagrammodelobject;
    }

    public void setModel_diagrammodelobject(model_DiagramModelObject model_diagrammodelobject) {
        this.model_diagrammodelobject = model_diagrammodelobject;
    }

}