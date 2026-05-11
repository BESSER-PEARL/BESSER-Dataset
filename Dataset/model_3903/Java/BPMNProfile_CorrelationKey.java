





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_CorrelationKey extends BaseElement {






    private BPMNProfile_CorrelationSubscription bpmnprofile_correlationsubscription;




    private List<BPMNProfile_CorrelationProperty> bpmnprofile_correlationpropertys;


    public BPMNProfile_CorrelationKey(
    ) {
        super(
        );
        this.bpmnprofile_correlationpropertys = new ArrayList<>();
    }

    public BPMNProfile_CorrelationKey(
        ArrayList<BPMNProfile_CorrelationProperty> bpmnprofile_correlationpropertys    ) {
        this.bpmnprofile_correlationpropertys = bpmnprofile_correlationpropertys;
    }


    public BPMNProfile_CorrelationSubscription getBpmnprofile_correlationsubscription() {
        return bpmnprofile_correlationsubscription;
    }

    public void setBpmnprofile_correlationsubscription(BPMNProfile_CorrelationSubscription bpmnprofile_correlationsubscription) {
        this.bpmnprofile_correlationsubscription = bpmnprofile_correlationsubscription;
    }
    public List<BPMNProfile_CorrelationProperty> getBpmnprofile_correlationpropertys() {
        return bpmnprofile_correlationpropertys;
    }

    public void addBpmnprofile_correlationproperty(Bpmnprofile_correlationproperty bpmnprofile_correlationproperty) {
        this.bpmnprofile_correlationpropertys.add(bpmnprofile_correlationproperty);
    }

}