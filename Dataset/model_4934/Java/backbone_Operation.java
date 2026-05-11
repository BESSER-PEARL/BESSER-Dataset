





import java.util.List;
import java.util.ArrayList;

public class backbone_Operation extends NamedElement {






    private backbone_Model backbone_model;




    private List<backbone_Parameter> backbone_parameters;




    private backbone_View backbone_view;


    public backbone_Operation(
    ) {
        super(
        );
        this.backbone_parameters = new ArrayList<>();
    }

    public backbone_Operation(
        ArrayList<backbone_Parameter> backbone_parameters    ) {
        this.backbone_parameters = backbone_parameters;
    }


    public backbone_Model getBackbone_model() {
        return backbone_model;
    }

    public void setBackbone_model(backbone_Model backbone_model) {
        this.backbone_model = backbone_model;
    }
    public List<backbone_Parameter> getBackbone_parameters() {
        return backbone_parameters;
    }

    public void addBackbone_parameter(Backbone_parameter backbone_parameter) {
        this.backbone_parameters.add(backbone_parameter);
    }
    public backbone_View getBackbone_view() {
        return backbone_view;
    }

    public void setBackbone_view(backbone_View backbone_view) {
        this.backbone_view = backbone_view;
    }

}