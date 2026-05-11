





import java.util.List;
import java.util.ArrayList;

public class editormodel_EStringToEObjectMapEntry  {

    private String key;





    private editormodel_EObject editormodel_eobject;


    public editormodel_EStringToEObjectMapEntry(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public editormodel_EObject getEditormodel_eobject() {
        return editormodel_eobject;
    }

    public void setEditormodel_eobject(editormodel_EObject editormodel_eobject) {
        this.editormodel_eobject = editormodel_eobject;
    }

}