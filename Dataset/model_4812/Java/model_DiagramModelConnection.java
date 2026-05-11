





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelConnection extends FontAttribute, DiagramModelComponent, Documentable, Properties {

    private int type;
    private String lineDecoration;
    private String text;





    private model_DiagramModelObject model_diagrammodelobject;




    private model_DiagramModelObject model_diagrammodelobject;




    private List<model_DiagramModelBendpoint> model_diagrammodelbendpoints;




    private model_DiagramModelObject model_diagrammodelobject;




    private model_DiagramModelObject model_diagrammodelobject;


    public model_DiagramModelConnection(
        int type,        String lineDecoration,        String text    ) {
        super(
        );
        this.type = type;
        this.lineDecoration = lineDecoration;
        this.text = text;
        this.model_diagrammodelbendpoints = new ArrayList<>();
    }

    public model_DiagramModelConnection(
        int type,        String lineDecoration,        String text        ArrayList<model_DiagramModelBendpoint> model_diagrammodelbendpoints    ) {
        this.type = type;
        this.lineDecoration = lineDecoration;
        this.text = text;
        this.model_diagrammodelbendpoints = model_diagrammodelbendpoints;
    }

    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getLinedecoration() {
        return lineDecoration;
    }

    public void setLinedecoration(String lineDecoration) {
        this.lineDecoration = lineDecoration;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public model_DiagramModelObject getModel_diagrammodelobject() {
        return model_diagrammodelobject;
    }

    public void setModel_diagrammodelobject(model_DiagramModelObject model_diagrammodelobject) {
        this.model_diagrammodelobject = model_diagrammodelobject;
    }
    public model_DiagramModelObject getModel_diagrammodelobject() {
        return model_diagrammodelobject;
    }

    public void setModel_diagrammodelobject(model_DiagramModelObject model_diagrammodelobject) {
        this.model_diagrammodelobject = model_diagrammodelobject;
    }
    public List<model_DiagramModelBendpoint> getModel_diagrammodelbendpoints() {
        return model_diagrammodelbendpoints;
    }

    public void addModel_diagrammodelbendpoint(Model_diagrammodelbendpoint model_diagrammodelbendpoint) {
        this.model_diagrammodelbendpoints.add(model_diagrammodelbendpoint);
    }
    public model_DiagramModelObject getModel_diagrammodelobject() {
        return model_diagrammodelobject;
    }

    public void setModel_diagrammodelobject(model_DiagramModelObject model_diagrammodelobject) {
        this.model_diagrammodelobject = model_diagrammodelobject;
    }
    public model_DiagramModelObject getModel_diagrammodelobject() {
        return model_diagrammodelobject;
    }

    public void setModel_diagrammodelobject(model_DiagramModelObject model_diagrammodelobject) {
        this.model_diagrammodelobject = model_diagrammodelobject;
    }

}