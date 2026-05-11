





import java.util.List;
import java.util.ArrayList;

public class dft_Observer extends GalileoNodeType {

    private String observationRate;





    private List<dft_GalileoFaultTreeNode> dft_galileofaulttreenodes;


    public dft_Observer(
        String observationRate    ) {
        super(
        );
        this.observationRate = observationRate;
        this.dft_galileofaulttreenodes = new ArrayList<>();
    }

    public dft_Observer(
        String observationRate        ArrayList<dft_GalileoFaultTreeNode> dft_galileofaulttreenodes    ) {
        this.observationRate = observationRate;
        this.dft_galileofaulttreenodes = dft_galileofaulttreenodes;
    }

    public String getObservationrate() {
        return observationRate;
    }

    public void setObservationrate(String observationRate) {
        this.observationRate = observationRate;
    }

    public List<dft_GalileoFaultTreeNode> getDft_galileofaulttreenodes() {
        return dft_galileofaulttreenodes;
    }

    public void addDft_galileofaulttreenode(Dft_galileofaulttreenode dft_galileofaulttreenode) {
        this.dft_galileofaulttreenodes.add(dft_galileofaulttreenode);
    }

}