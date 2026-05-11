





import java.util.List;
import java.util.ArrayList;

public class aggregator_Contribution extends StatusProvider, InfosProvider, DescriptionProvider, EnabledStatusProvider, IdentificationProvider {

    private String label;





    private List<aggregator_Contact> aggregator_contacts;


    public aggregator_Contribution(
        String label    ) {
        super(
        );
        this.label = label;
        this.aggregator_contacts = new ArrayList<>();
    }

    public aggregator_Contribution(
        String label        ArrayList<aggregator_Contact> aggregator_contacts    ) {
        this.label = label;
        this.aggregator_contacts = aggregator_contacts;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<aggregator_Contact> getAggregator_contacts() {
        return aggregator_contacts;
    }

    public void addAggregator_contact(Aggregator_contact aggregator_contact) {
        this.aggregator_contacts.add(aggregator_contact);
    }

}