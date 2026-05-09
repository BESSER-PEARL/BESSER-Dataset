





import java.util.List;
import java.util.ArrayList;

public class model_GeppettoModel  {

    private String id;
    private String name;





    private List<model_GeppettoLibrary> model_geppettolibrarys;




    private List<model_Tag> model_tags;




    private List<model_World> model_worlds;


    public model_GeppettoModel(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
        this.model_geppettolibrarys = new ArrayList<>();
        this.model_tags = new ArrayList<>();
        this.model_worlds = new ArrayList<>();
    }

    public model_GeppettoModel(
        String id,        String name        ArrayList<model_GeppettoLibrary> model_geppettolibrarys,        ArrayList<model_Tag> model_tags,        ArrayList<model_World> model_worlds    ) {
        this.id = id;
        this.name = name;
        this.model_geppettolibrarys = model_geppettolibrarys;
        this.model_tags = model_tags;
        this.model_worlds = model_worlds;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<model_GeppettoLibrary> getModel_geppettolibrarys() {
        return model_geppettolibrarys;
    }

    public void addModel_geppettolibrary(Model_geppettolibrary model_geppettolibrary) {
        this.model_geppettolibrarys.add(model_geppettolibrary);
    }
    public List<model_Tag> getModel_tags() {
        return model_tags;
    }

    public void addModel_tag(Model_tag model_tag) {
        this.model_tags.add(model_tag);
    }
    public List<model_World> getModel_worlds() {
        return model_worlds;
    }

    public void addModel_world(Model_world model_world) {
        this.model_worlds.add(model_world);
    }

}