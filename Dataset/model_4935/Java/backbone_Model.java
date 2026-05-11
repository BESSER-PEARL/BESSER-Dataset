





import java.util.List;
import java.util.ArrayList;

public class backbone_Model extends NamedElement {






    private List<backbone_Reference> backbone_references;




    private List<backbone_Operation> backbone_operations;




    private List<backbone_Attribute> backbone_attributes;




    private backbone_Application backbone_application;




    private backbone_Collection backbone_collection;




    private backbone_Application backbone_application;




    private backbone_Reference backbone_reference;


    public backbone_Model(
    ) {
        super(
        );
        this.backbone_references = new ArrayList<>();
        this.backbone_operations = new ArrayList<>();
        this.backbone_attributes = new ArrayList<>();
    }

    public backbone_Model(
        ArrayList<backbone_Reference> backbone_references,        ArrayList<backbone_Operation> backbone_operations,        ArrayList<backbone_Attribute> backbone_attributes    ) {
        this.backbone_references = backbone_references;
        this.backbone_operations = backbone_operations;
        this.backbone_attributes = backbone_attributes;
    }


    public List<backbone_Reference> getBackbone_references() {
        return backbone_references;
    }

    public void addBackbone_reference(Backbone_reference backbone_reference) {
        this.backbone_references.add(backbone_reference);
    }
    public List<backbone_Operation> getBackbone_operations() {
        return backbone_operations;
    }

    public void addBackbone_operation(Backbone_operation backbone_operation) {
        this.backbone_operations.add(backbone_operation);
    }
    public List<backbone_Attribute> getBackbone_attributes() {
        return backbone_attributes;
    }

    public void addBackbone_attribute(Backbone_attribute backbone_attribute) {
        this.backbone_attributes.add(backbone_attribute);
    }
    public backbone_Application getBackbone_application() {
        return backbone_application;
    }

    public void setBackbone_application(backbone_Application backbone_application) {
        this.backbone_application = backbone_application;
    }
    public backbone_Collection getBackbone_collection() {
        return backbone_collection;
    }

    public void setBackbone_collection(backbone_Collection backbone_collection) {
        this.backbone_collection = backbone_collection;
    }
    public backbone_Application getBackbone_application() {
        return backbone_application;
    }

    public void setBackbone_application(backbone_Application backbone_application) {
        this.backbone_application = backbone_application;
    }
    public backbone_Reference getBackbone_reference() {
        return backbone_reference;
    }

    public void setBackbone_reference(backbone_Reference backbone_reference) {
        this.backbone_reference = backbone_reference;
    }

}