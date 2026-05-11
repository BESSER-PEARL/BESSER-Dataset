





import java.util.List;
import java.util.ArrayList;

public class editormodel_Dimension  {

    private int height;
    private int width;





    private editormodel_VisualModel editormodel_visualmodel;


    public editormodel_Dimension(
        int height,        int width    ) {
        this.height = height;
        this.width = width;
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

    public editormodel_VisualModel getEditormodel_visualmodel() {
        return editormodel_visualmodel;
    }

    public void setEditormodel_visualmodel(editormodel_VisualModel editormodel_visualmodel) {
        this.editormodel_visualmodel = editormodel_visualmodel;
    }

}