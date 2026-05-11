





import java.util.List;
import java.util.ArrayList;

public class aggregator_ValidationSet extends EnabledStatusProvider, IdentificationProvider, InfosProvider, DescriptionProvider, StatusProvider {

    private String label;
    private boolean extension;
    private boolean abstract;





    private List<aggregator_ValidationSet> aggregator_validationsets;


    public aggregator_ValidationSet(
        String label,        boolean extension,        boolean abstract    ) {
        super(
        );
        this.label = label;
        this.extension = extension;
        this.abstract = abstract;
        this.aggregator_validationsets = new ArrayList<>();
    }

    public aggregator_ValidationSet(
        String label,        boolean extension,        boolean abstract        ArrayList<aggregator_ValidationSet> aggregator_validationsets    ) {
        this.label = label;
        this.extension = extension;
        this.abstract = abstract;
        this.aggregator_validationsets = aggregator_validationsets;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public boolean getExtension() {
        return extension;
    }

    public void setExtension(boolean extension) {
        this.extension = extension;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public List<aggregator_ValidationSet> getAggregator_validationsets() {
        return aggregator_validationsets;
    }

    public void addAggregator_validationset(Aggregator_validationset aggregator_validationset) {
        this.aggregator_validationsets.add(aggregator_validationset);
    }

}