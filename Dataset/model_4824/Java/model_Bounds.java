





import java.util.List;
import java.util.ArrayList;

public class model_Bounds  {

    private int x;
    private int height;
    private int y;
    private int width;





    private model_DiagramModelObject model_diagrammodelobject;


    public model_Bounds(
        int x,        int height,        int y,        int width    ) {
        this.x = x;
        this.height = height;
        this.y = y;
        this.width = width;
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

    public model_DiagramModelObject getModel_diagrammodelobject() {
        return model_diagrammodelobject;
    }

    public void setModel_diagrammodelobject(model_DiagramModelObject model_diagrammodelobject) {
        this.model_diagrammodelobject = model_diagrammodelobject;
    }

}