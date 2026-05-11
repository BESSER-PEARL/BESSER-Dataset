





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation extends SpecifiedQoSAnnotation {






    private List<ExternalFailureOccurrenceDescription> externalfailureoccurrencedescriptions;


    public pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation(
    ) {
        super(
        );
        this.externalfailureoccurrencedescriptions = new ArrayList<>();
    }

    public pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation(
        ArrayList<ExternalFailureOccurrenceDescription> externalfailureoccurrencedescriptions    ) {
        this.externalfailureoccurrencedescriptions = externalfailureoccurrencedescriptions;
    }


    public List<ExternalFailureOccurrenceDescription> getExternalfailureoccurrencedescriptions() {
        return externalfailureoccurrencedescriptions;
    }

    public void addExternalfailureoccurrencedescription(Externalfailureoccurrencedescription externalfailureoccurrencedescription) {
        this.externalfailureoccurrencedescriptions.add(externalfailureoccurrencedescription);
    }

}