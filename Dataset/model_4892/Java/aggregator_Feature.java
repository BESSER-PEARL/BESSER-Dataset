





import java.util.List;
import java.util.ArrayList;

public class aggregator_Feature extends MappedUnit {






    private aggregator_MappedRepository aggregator_mappedrepository;




    private List<aggregator_CustomCategory> aggregator_customcategorys;




    private aggregator_CustomCategory aggregator_customcategory;


    public aggregator_Feature(
    ) {
        super(
        );
        this.aggregator_customcategorys = new ArrayList<>();
    }

    public aggregator_Feature(
        ArrayList<aggregator_CustomCategory> aggregator_customcategorys    ) {
        this.aggregator_customcategorys = aggregator_customcategorys;
    }


    public aggregator_MappedRepository getAggregator_mappedrepository() {
        return aggregator_mappedrepository;
    }

    public void setAggregator_mappedrepository(aggregator_MappedRepository aggregator_mappedrepository) {
        this.aggregator_mappedrepository = aggregator_mappedrepository;
    }
    public List<aggregator_CustomCategory> getAggregator_customcategorys() {
        return aggregator_customcategorys;
    }

    public void addAggregator_customcategory(Aggregator_customcategory aggregator_customcategory) {
        this.aggregator_customcategorys.add(aggregator_customcategory);
    }
    public aggregator_CustomCategory getAggregator_customcategory() {
        return aggregator_customcategory;
    }

    public void setAggregator_customcategory(aggregator_CustomCategory aggregator_customcategory) {
        this.aggregator_customcategory = aggregator_customcategory;
    }

}