





import java.util.List;
import java.util.ArrayList;

public class editormodel_NodeVisualModel extends VisualModel {

    private String rotation;



    public editormodel_NodeVisualModel(
        String rotation    ) {
        super(
        );
        this.rotation = rotation;
    }


    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }


}