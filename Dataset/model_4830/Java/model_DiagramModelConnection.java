





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelConnection extends Properties, Documentable, LineObject, FontAttribute, Connectable {

    private String text;
    private int type;
    private int textPosition;





    private List<model_DiagramModelBendpoint> model_diagrammodelbendpoints;


    public model_DiagramModelConnection(
        String text,        int type,        int textPosition    ) {
        super(
        );
        this.text = text;
        this.type = type;
        this.textPosition = textPosition;
        this.model_diagrammodelbendpoints = new ArrayList<>();
    }

    public model_DiagramModelConnection(
        String text,        int type,        int textPosition        ArrayList<model_DiagramModelBendpoint> model_diagrammodelbendpoints    ) {
        this.text = text;
        this.type = type;
        this.textPosition = textPosition;
        this.model_diagrammodelbendpoints = model_diagrammodelbendpoints;
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
    public int getTextposition() {
        return textPosition;
    }

    public void setTextposition(int textPosition) {
        this.textPosition = textPosition;
    }

    public List<model_DiagramModelBendpoint> getModel_diagrammodelbendpoints() {
        return model_diagrammodelbendpoints;
    }

    public void addModel_diagrammodelbendpoint(Model_diagrammodelbendpoint model_diagrammodelbendpoint) {
        this.model_diagrammodelbendpoints.add(model_diagrammodelbendpoint);
    }

}