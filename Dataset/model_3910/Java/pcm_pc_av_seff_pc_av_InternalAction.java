





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_seff_pc_av_InternalAction extends AbstractInternalControlFlowAction {






    private List<InternalFailureOccurrenceDescription> internalfailureoccurrencedescriptions;


    public pcm_pc_av_seff_pc_av_InternalAction(
    ) {
        super(
        );
        this.internalfailureoccurrencedescriptions = new ArrayList<>();
    }

    public pcm_pc_av_seff_pc_av_InternalAction(
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