





import java.util.List;
import java.util.ArrayList;

public class model_Edge extends OnoObject {

    private String type;





    private List<model_LabelPos> model_labelposs;




    private model_Diagram model_diagram;




    private model_RolePlayerConstraint model_roleplayerconstraint;


    public model_Edge(
        String type    ) {
        super(
        );
        this.type = type;
        this.model_labelposs = new ArrayList<>();
    }

    public model_Edge(
        String type        ArrayList<model_LabelPos> model_labelposs    ) {
        this.type = type;
        this.model_labelposs = model_labelposs;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<model_LabelPos> getModel_labelposs() {
        return model_labelposs;
    }

    public void addModel_labelpos(Model_labelpos model_labelpos) {
        this.model_labelposs.add(model_labelpos);
    }
    public model_Diagram getModel_diagram() {
        return model_diagram;
    }

    public void setModel_diagram(model_Diagram model_diagram) {
        this.model_diagram = model_diagram;
    }
    public model_RolePlayerConstraint getModel_roleplayerconstraint() {
        return model_roleplayerconstraint;
    }

    public void setModel_roleplayerconstraint(model_RolePlayerConstraint model_roleplayerconstraint) {
        this.model_roleplayerconstraint = model_roleplayerconstraint;
    }

}