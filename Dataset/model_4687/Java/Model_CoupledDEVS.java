





import java.util.List;
import java.util.ArrayList;

public class Model_CoupledDEVS extends DEVS {






    private List<Model_DEVS> model_devss;


    public Model_CoupledDEVS(
    ) {
        super(
        );
        this.model_devss = new ArrayList<>();
    }

    public Model_CoupledDEVS(
        ArrayList<Model_DEVS> model_devss    ) {
        this.model_devss = model_devss;
    }


    public List<Model_DEVS> getModel_devss() {
        return model_devss;
    }

    public void addModel_devs(Model_devs model_devs) {
        this.model_devss.add(model_devs);
    }

}