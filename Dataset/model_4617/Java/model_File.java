





import java.util.List;
import java.util.ArrayList;

public class model_File extends OnoObject {

    private String notes;
    private String filename;
    private boolean dirty;





    private List<model_Diagram> model_diagrams;




    private model_TopicMapSchema model_topicmapschema;


    public model_File(
        String notes,        String filename,        boolean dirty    ) {
        super(
        );
        this.notes = notes;
        this.filename = filename;
        this.dirty = dirty;
        this.model_diagrams = new ArrayList<>();
    }

    public model_File(
        String notes,        String filename,        boolean dirty        ArrayList<model_Diagram> model_diagrams    ) {
        this.notes = notes;
        this.filename = filename;
        this.dirty = dirty;
        this.model_diagrams = model_diagrams;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }
    public boolean getDirty() {
        return dirty;
    }

    public void setDirty(boolean dirty) {
        this.dirty = dirty;
    }

    public List<model_Diagram> getModel_diagrams() {
        return model_diagrams;
    }

    public void addModel_diagram(Model_diagram model_diagram) {
        this.model_diagrams.add(model_diagram);
    }
    public model_TopicMapSchema getModel_topicmapschema() {
        return model_topicmapschema;
    }

    public void setModel_topicmapschema(model_TopicMapSchema model_topicmapschema) {
        this.model_topicmapschema = model_topicmapschema;
    }

}