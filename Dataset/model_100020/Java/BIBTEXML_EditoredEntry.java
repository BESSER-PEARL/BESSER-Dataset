





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_EditoredEntry extends Entry {

    private String editor;



    public BIBTEXML_EditoredEntry(
        String editor    ) {
        super(
        );
        this.editor = editor;
    }


    public String getEditor() {
        return editor;
    }

    public void setEditor(String editor) {
        this.editor = editor;
    }


}