





import java.util.List;
import java.util.ArrayList;

public class model_Link extends BPELExtensibleElement {

    private String name;





    private model_Source model_source;




    private model_Links model_links;




    private List<model_Source> model_sources;


    public model_Link(
        String name    ) {
        super(
        );
        this.name = name;
        this.model_sources = new ArrayList<>();
    }

    public model_Link(
        String name        ArrayList<model_Source> model_sources    ) {
        this.name = name;
        this.model_sources = model_sources;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Source getModel_source() {
        return model_source;
    }

    public void setModel_source(model_Source model_source) {
        this.model_source = model_source;
    }
    public model_Links getModel_links() {
        return model_links;
    }

    public void setModel_links(model_Links model_links) {
        this.model_links = model_links;
    }
    public List<model_Source> getModel_sources() {
        return model_sources;
    }

    public void addModel_source(Model_source model_source) {
        this.model_sources.add(model_source);
    }

}