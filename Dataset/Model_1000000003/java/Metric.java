





import java.util.List;
import java.util.ArrayList;

public class Metric extends AssessmentElement {






    private List<Derived> deriveds;




    private List<MetricCategory> metriccategorys;


    public Metric(
    ) {
        super(
            String,            name,            String,            description        );
        this.deriveds = new ArrayList<>();
        this.metriccategorys = new ArrayList<>();
    }

    public Metric(
        ArrayList<Derived> deriveds,        ArrayList<MetricCategory> metriccategorys    ) {
        this.deriveds = deriveds;
        this.metriccategorys = metriccategorys;
    }


    public List<Derived> getDeriveds() {
        return deriveds;
    }

    public void addDerived(Derived derived) {
        this.deriveds.add(derived);
    }
    public List<MetricCategory> getMetriccategorys() {
        return metriccategorys;
    }

    public void addMetriccategory(Metriccategory metriccategory) {
        this.metriccategorys.add(metriccategory);
    }

}