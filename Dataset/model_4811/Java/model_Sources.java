





import java.util.List;
import java.util.ArrayList;

public class model_Sources extends BPELExtensibleElement {






    private List<model_Source> model_sources;


    public model_Sources(
    ) {
        super(
        );
        this.model_sources = new ArrayList<>();
    }

    public model_Sources(
        ArrayList<model_Source> model_sources    ) {
        this.model_sources = model_sources;
    }


    public List<model_Source> getModel_sources() {
        return model_sources;
    }

    public void addModel_source(Model_source model_source) {
        this.model_sources.add(model_source);
    }

}