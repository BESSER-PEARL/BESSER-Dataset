





import java.util.List;
import java.util.ArrayList;

public class aggregator_ValidationSet extends EnabledStatusProvider, InfosProvider, StatusProvider, DescriptionProvider, IdentificationProvider {

    private String label;
    private boolean abstract;
    private boolean extension;





    private aggregator_ValidationSet aggregator_validationset;


    public aggregator_ValidationSet(
        String label,        boolean abstract,        boolean extension    ) {
        super(
        );
        this.label = label;
        this.abstract = abstract;
        this.extension = extension;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getExtension() {
        return extension;
    }

    public void setExtension(boolean extension) {
        this.extension = extension;
    }

    public aggregator_ValidationSet getAggregator_validationset() {
        return aggregator_validationset;
    }

    public void setAggregator_validationset(aggregator_ValidationSet aggregator_validationset) {
        this.aggregator_validationset = aggregator_validationset;
    }

}