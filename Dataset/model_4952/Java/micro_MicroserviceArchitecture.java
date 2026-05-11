





import java.util.List;
import java.util.ArrayList;

public class micro_MicroserviceArchitecture extends NamedElement {






    private List<micro_Model> micro_models;


    public micro_MicroserviceArchitecture(
    ) {
        super(
        );
        this.micro_models = new ArrayList<>();
    }

    public micro_MicroserviceArchitecture(
        ArrayList<micro_Model> micro_models    ) {
        this.micro_models = micro_models;
    }


    public List<micro_Model> getMicro_models() {
        return micro_models;
    }

    public void addMicro_model(Micro_model micro_model) {
        this.micro_models.add(micro_model);
    }

}