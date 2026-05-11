





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_reliability_pc_SoftwareInducedFailureType extends FailureType {






    private List<InternalFailureOccurrenceDescription> internalfailureoccurrencedescriptions;


    public pcm_pc_reliability_pc_SoftwareInducedFailureType(
    ) {
        super(
        );
        this.internalfailureoccurrencedescriptions = new ArrayList<>();
    }

    public pcm_pc_reliability_pc_SoftwareInducedFailureType(
        ArrayList<InternalFailureOccurrenceDescription> internalfailureoccurrencedescriptions    ) {
        this.internalfailureoccurrencedescriptions = internalfailureoccurrencedescriptions;
    }


    public List<InternalFailureOccurrenceDescription> getInternalfailureoccurrencedescriptions() {
        return internalfailureoccurrencedescriptions;
    }

    public void addInternalfailureoccurrencedescription(Internalfailureoccurrencedescription internalfailureoccurrencedescription) {
        this.internalfailureoccurrencedescriptions.add(internalfailureoccurrencedescription);
    }

}