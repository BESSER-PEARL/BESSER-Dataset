





import java.util.List;
import java.util.ArrayList;

public class gmf_all_mappings_FeatureLabelMapping extends LabelMapping {

    private String viewPattern;
    private String editorPattern;
    private String editMethod;
    private String viewMethod;
    private String editPattern;



    public gmf_all_mappings_FeatureLabelMapping(
        String viewPattern,        String editorPattern,        String editMethod,        String viewMethod,        String editPattern    ) {
        super(
        );
        this.viewPattern = viewPattern;
        this.editorPattern = editorPattern;
        this.editMethod = editMethod;
        this.viewMethod = viewMethod;
        this.editPattern = editPattern;
    }


    public String getViewpattern() {
        return viewPattern;
    }

    public void setViewpattern(String viewPattern) {
        this.viewPattern = viewPattern;
    }
    public String getEditorpattern() {
        return editorPattern;
    }

    public void setEditorpattern(String editorPattern) {
        this.editorPattern = editorPattern;
    }
    public String getEditmethod() {
        return editMethod;
    }

    public void setEditmethod(String editMethod) {
        this.editMethod = editMethod;
    }
    public String getViewmethod() {
        return viewMethod;
    }

    public void setViewmethod(String viewMethod) {
        this.viewMethod = viewMethod;
    }
    public String getEditpattern() {
        return editPattern;
    }

    public void setEditpattern(String editPattern) {
        this.editPattern = editPattern;
    }


}