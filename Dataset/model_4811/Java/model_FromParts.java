





import java.util.List;
import java.util.ArrayList;

public class model_FromParts extends BPELExtensibleElement {






    private List<model_FromPart> model_fromparts;


    public model_FromParts(
    ) {
        super(
        );
        this.model_fromparts = new ArrayList<>();
    }

    public model_FromParts(
        ArrayList<model_FromPart> model_fromparts    ) {
        this.model_fromparts = model_fromparts;
    }


    public List<model_FromPart> getModel_fromparts() {
        return model_fromparts;
    }

    public void addModel_frompart(Model_frompart model_frompart) {
        this.model_fromparts.add(model_frompart);
    }

}