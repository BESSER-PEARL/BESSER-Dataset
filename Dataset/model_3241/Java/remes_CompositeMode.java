





import java.util.List;
import java.util.ArrayList;

public class remes_CompositeMode extends Mode {






    private List<remes_ConditionalConnector> remes_conditionalconnectors;




    private remes_ConditionalConnector remes_conditionalconnector;


    public remes_CompositeMode(
    ) {
        super(
        );
        this.remes_conditionalconnectors = new ArrayList<>();
    }

    public remes_CompositeMode(
        ArrayList<remes_ConditionalConnector> remes_conditionalconnectors    ) {
        this.remes_conditionalconnectors = remes_conditionalconnectors;
    }


    public List<remes_ConditionalConnector> getRemes_conditionalconnectors() {
        return remes_conditionalconnectors;
    }

    public void addRemes_conditionalconnector(Remes_conditionalconnector remes_conditionalconnector) {
        this.remes_conditionalconnectors.add(remes_conditionalconnector);
    }
    public remes_ConditionalConnector getRemes_conditionalconnector() {
        return remes_conditionalconnector;
    }

    public void setRemes_conditionalconnector(remes_ConditionalConnector remes_conditionalconnector) {
        this.remes_conditionalconnector = remes_conditionalconnector;
    }

}