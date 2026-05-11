





import java.util.List;
import java.util.ArrayList;

public class model_ToParts extends BPELExtensibleElement {






    private List<model_ToPart> model_toparts;


    public model_ToParts(
    ) {
        super(
        );
        this.model_toparts = new ArrayList<>();
    }

    public model_ToParts(
        ArrayList<model_ToPart> model_toparts    ) {
        this.model_toparts = model_toparts;
    }


    public List<model_ToPart> getModel_toparts() {
        return model_toparts;
    }

    public void addModel_topart(Model_topart model_topart) {
        this.model_toparts.add(model_topart);
    }

}