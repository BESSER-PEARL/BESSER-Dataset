





import java.util.List;
import java.util.ArrayList;

public class model_BNode  {

    private int id;





    private List<model_BNode> model_bnodes;


    public model_BNode(
        int id    ) {
        this.id = id;
        this.model_bnodes = new ArrayList<>();
    }

    public model_BNode(
        int id        ArrayList<model_BNode> model_bnodes    ) {
        this.id = id;
        this.model_bnodes = model_bnodes;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<model_BNode> getModel_bnodes() {
        return model_bnodes;
    }

    public void addModel_bnode(Model_bnode model_bnode) {
        this.model_bnodes.add(model_bnode);
    }

}