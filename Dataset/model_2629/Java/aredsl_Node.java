





import java.util.List;
import java.util.ArrayList;

public class aredsl_Node  {

    private String description;
    private String contaimentKind;
    private String id;
    private String semantics;





    private List<aredsl_Node> aredsl_nodes;


    public aredsl_Node(
        String description,        String contaimentKind,        String id,        String semantics    ) {
        this.description = description;
        this.contaimentKind = contaimentKind;
        this.id = id;
        this.semantics = semantics;
        this.aredsl_nodes = new ArrayList<>();
    }

    public aredsl_Node(
        String description,        String contaimentKind,        String id,        String semantics        ArrayList<aredsl_Node> aredsl_nodes    ) {
        this.description = description;
        this.contaimentKind = contaimentKind;
        this.id = id;
        this.semantics = semantics;
        this.aredsl_nodes = aredsl_nodes;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getContaimentkind() {
        return contaimentKind;
    }

    public void setContaimentkind(String contaimentKind) {
        this.contaimentKind = contaimentKind;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSemantics() {
        return semantics;
    }

    public void setSemantics(String semantics) {
        this.semantics = semantics;
    }

    public List<aredsl_Node> getAredsl_nodes() {
        return aredsl_nodes;
    }

    public void addAredsl_node(Aredsl_node aredsl_node) {
        this.aredsl_nodes.add(aredsl_node);
    }

}