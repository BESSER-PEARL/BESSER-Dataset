





import java.util.List;
import java.util.ArrayList;

public class model_BNode  {

    private int id;





    private model_BNode model_bnode;


    public model_BNode(
        int id    ) {
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public model_BNode getModel_bnode() {
        return model_bnode;
    }

    public void setModel_bnode(model_BNode model_bnode) {
        this.model_bnode = model_bnode;
    }

}