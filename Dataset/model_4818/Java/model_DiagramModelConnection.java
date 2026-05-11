





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelConnection extends Connectable, LineObject, Documentable, FontAttribute, Properties {

    private int textPosition;
    private String text;
    private int type;





    private List<model_DiagramModelBendpoint> model_diagrammodelbendpoints;


    public model_DiagramModelConnection(
        int textPosition,        String text,        int type    ) {
        super(
        );
        this.textPosition = textPosition;
        this.text = text;
        this.type = type;
        this.model_diagrammodelbendpoints = new ArrayList<>();
    }

    public model_DiagramModelConnection(
        int textPosition,        String text,        int type        ArrayList<model_DiagramModelBendpoint> model_diagrammodelbendpoints    ) {
        this.textPosition = textPosition;
        this.text = text;
        this.type = type;
        this.model_diagrammodelbendpoints = model_diagrammodelbendpoints;
    }

    public int getTextposition() {
        return textPosition;
    }

    public void setTextposition(int textPosition) {
        this.textPosition = textPosition;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }

    public List<model_DiagramModelBendpoint> getModel_diagrammodelbendpoints() {
        return model_diagrammodelbendpoints;
    }

    public void addModel_diagrammodelbendpoint(Model_diagrammodelbendpoint model_diagrammodelbendpoint) {
        this.model_diagrammodelbendpoints.add(model_diagrammodelbendpoint);
    }

}