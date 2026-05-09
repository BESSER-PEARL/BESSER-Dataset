





import java.util.List;
import java.util.ArrayList;

public class model_Node extends ISynchable {

    private String name;
    private String id;





    private List<model_Tag> model_tags;


    public model_Node(
        String name,        String id    ) {
        super(
        );
        this.name = name;
        this.id = id;
        this.model_tags = new ArrayList<>();
    }

    public model_Node(
        String name,        String id        ArrayList<model_Tag> model_tags    ) {
        this.name = name;
        this.id = id;
        this.model_tags = model_tags;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<model_Tag> getModel_tags() {
        return model_tags;
    }

    public void addModel_tag(Model_tag model_tag) {
        this.model_tags.add(model_tag);
    }

}