





import java.util.List;
import java.util.ArrayList;

public class editormodel_Point  {

    private int x;
    private int y;





    private editormodel_VisualModel editormodel_visualmodel;


    public editormodel_Point(
        int x,        int y    ) {
        this.x = x;
        this.y = y;
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

    public editormodel_VisualModel getEditormodel_visualmodel() {
        return editormodel_visualmodel;
    }

    public void setEditormodel_visualmodel(editormodel_VisualModel editormodel_visualmodel) {
        this.editormodel_visualmodel = editormodel_visualmodel;
    }

}