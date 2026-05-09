





import java.util.List;
import java.util.ArrayList;

public class model_BookBNode  {

    private String title;





    private model_PersonBNode model_personbnode;




    private List<model_PersonBNode> model_personbnodes;


    public model_BookBNode(
        String title    ) {
        this.title = title;
        this.model_personbnodes = new ArrayList<>();
    }

    public model_BookBNode(
        String title        ArrayList<model_PersonBNode> model_personbnodes    ) {
        this.title = title;
        this.model_personbnodes = model_personbnodes;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public model_PersonBNode getModel_personbnode() {
        return model_personbnode;
    }

    public void setModel_personbnode(model_PersonBNode model_personbnode) {
        this.model_personbnode = model_personbnode;
    }
    public List<model_PersonBNode> getModel_personbnodes() {
        return model_personbnodes;
    }

    public void addModel_personbnode(Model_personbnode model_personbnode) {
        this.model_personbnodes.add(model_personbnode);
    }

}