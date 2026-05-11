





import java.util.List;
import java.util.ArrayList;

public class backbone_View extends NamedElement {






    private backbone_Application backbone_application;




    private List<backbone_Operation> backbone_operations;




    private backbone_Application backbone_application;


    public backbone_View(
    ) {
        super(
        );
        this.backbone_operations = new ArrayList<>();
    }

    public backbone_View(
        ArrayList<backbone_Operation> backbone_operations    ) {
        this.backbone_operations = backbone_operations;
    }


    public backbone_Application getBackbone_application() {
        return backbone_application;
    }

    public void setBackbone_application(backbone_Application backbone_application) {
        this.backbone_application = backbone_application;
    }
    public List<backbone_Operation> getBackbone_operations() {
        return backbone_operations;
    }

    public void addBackbone_operation(Backbone_operation backbone_operation) {
        this.backbone_operations.add(backbone_operation);
    }
    public backbone_Application getBackbone_application() {
        return backbone_application;
    }

    public void setBackbone_application(backbone_Application backbone_application) {
        this.backbone_application = backbone_application;
    }

}