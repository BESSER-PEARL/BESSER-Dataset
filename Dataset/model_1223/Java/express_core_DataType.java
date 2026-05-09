





import java.util.List;
import java.util.ArrayList;

public class express_core_DataType  {






    private List<Instance> instances;


    public express_core_DataType(
    ) {
        this.instances = new ArrayList<>();
    }

    public express_core_DataType(
        ArrayList<Instance> instances    ) {
        this.instances = instances;
    }


    public List<Instance> getInstances() {
        return instances;
    }

    public void addInstance(Instance instance) {
        this.instances.add(instance);
    }

}