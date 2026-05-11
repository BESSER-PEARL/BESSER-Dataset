





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_seff_av_pc_InternalAction extends AbstractInternalControlFlowAction {






    private List<InternalFailureOccurrenceDescription> internalfailureoccurrencedescriptions;


    public pcm_av_pc_seff_av_pc_InternalAction(
    ) {
        super(
        );
        this.internalfailureoccurrencedescriptions = new ArrayList<>();
    }

    public pcm_av_pc_seff_av_pc_InternalAction(
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