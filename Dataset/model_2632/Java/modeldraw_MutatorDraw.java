





import java.util.List;
import java.util.ArrayList;

public class modeldraw_MutatorDraw extends Item {

    private String metamodel;
    private String type;





    private List<modeldraw_Content> modeldraw_contents;




    private List<modeldraw_Relation> modeldraw_relations;




    private List<modeldraw_Node> modeldraw_nodes;


    public modeldraw_MutatorDraw(
        String metamodel,        String type    ) {
        super(
        );
        this.metamodel = metamodel;
        this.type = type;
        this.modeldraw_contents = new ArrayList<>();
        this.modeldraw_relations = new ArrayList<>();
        this.modeldraw_nodes = new ArrayList<>();
    }

    public modeldraw_MutatorDraw(
        String metamodel,        String type        ArrayList<modeldraw_Content> modeldraw_contents,        ArrayList<modeldraw_Relation> modeldraw_relations,        ArrayList<modeldraw_Node> modeldraw_nodes    ) {
        this.metamodel = metamodel;
        this.type = type;
        this.modeldraw_contents = modeldraw_contents;
        this.modeldraw_relations = modeldraw_relations;
        this.modeldraw_nodes = modeldraw_nodes;
    }

    public String getMetamodel() {
        return metamodel;
    }

    public void setMetamodel(String metamodel) {
        this.metamodel = metamodel;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<modeldraw_Content> getModeldraw_contents() {
        return modeldraw_contents;
    }

    public void addModeldraw_content(Modeldraw_content modeldraw_content) {
        this.modeldraw_contents.add(modeldraw_content);
    }
    public List<modeldraw_Relation> getModeldraw_relations() {
        return modeldraw_relations;
    }

    public void addModeldraw_relation(Modeldraw_relation modeldraw_relation) {
        this.modeldraw_relations.add(modeldraw_relation);
    }
    public List<modeldraw_Node> getModeldraw_nodes() {
        return modeldraw_nodes;
    }

    public void addModeldraw_node(Modeldraw_node modeldraw_node) {
        this.modeldraw_nodes.add(modeldraw_node);
    }

}