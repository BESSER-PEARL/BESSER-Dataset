





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_qosannotations_av_pc_QoSAnnotations extends Entity {






    private List<SpecifiedOutputParameterAbstraction> specifiedoutputparameterabstractions;


    public pcm_av_pc_qosannotations_av_pc_QoSAnnotations(
    ) {
        super(
        );
        this.specifiedoutputparameterabstractions = new ArrayList<>();
    }

    public pcm_av_pc_qosannotations_av_pc_QoSAnnotations(
        ArrayList<SpecifiedOutputParameterAbstraction> specifiedoutputparameterabstractions    ) {
        this.specifiedoutputparameterabstractions = specifiedoutputparameterabstractions;
    }


    public List<SpecifiedOutputParameterAbstraction> getSpecifiedoutputparameterabstractions() {
        return specifiedoutputparameterabstractions;
    }

    public void addSpecifiedoutputparameterabstraction(Specifiedoutputparameterabstraction specifiedoutputparameterabstraction) {
        this.specifiedoutputparameterabstractions.add(specifiedoutputparameterabstraction);
    }

}