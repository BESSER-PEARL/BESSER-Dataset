





import java.util.List;
import java.util.ArrayList;

public class model_Tag extends ISynchable {

    private String name;





    private List<model_Tag> model_tags;




    private model_GeppettoModel model_geppettomodel;


    public model_Tag(
        String name    ) {
        super(
        );
        this.name = name;
        this.model_tags = new ArrayList<>();
    }

    public model_Tag(
        String name        ArrayList<model_Tag> model_tags    ) {
        this.name = name;
        this.model_tags = model_tags;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<model_Tag> getModel_tags() {
        return model_tags;
    }

    public void addModel_tag(Model_tag model_tag) {
        this.model_tags.add(model_tag);
    }
    public model_GeppettoModel getModel_geppettomodel() {
        return model_geppettomodel;
    }

    public void setModel_geppettomodel(model_GeppettoModel model_geppettomodel) {
        this.model_geppettomodel = model_geppettomodel;
    }

}