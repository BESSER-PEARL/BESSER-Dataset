





import java.util.List;
import java.util.ArrayList;

public class simplepdl_RessourceInstance extends ProcessElement {

    private int instances;



    public simplepdl_RessourceInstance(
        int instances    ) {
        super(
        );
        this.instances = instances;
    }


    public int getInstances() {
        return instances;
    }

    public void setInstances(int instances) {
        this.instances = instances;
    }


}