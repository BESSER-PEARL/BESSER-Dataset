





import java.util.List;
import java.util.ArrayList;

public class oaam_allocations_SignalToMessageAssignment  {

    private int position;





    private Signal signal;




    private List<Variant> variants;




    private DataTypeA datatypea;




    private SignalInMessageCapability signalinmessagecapability;




    private List<AttributeA> attributeas;




    private List<OperationModeReference> operationmodereferences;


    public oaam_allocations_SignalToMessageAssignment(
        int position    ) {
        this.position = position;
        this.variants = new ArrayList<>();
        this.attributeas = new ArrayList<>();
        this.operationmodereferences = new ArrayList<>();
    }

    public oaam_allocations_SignalToMessageAssignment(
        int position        ArrayList<Variant> variants,        ArrayList<AttributeA> attributeas,        ArrayList<OperationModeReference> operationmodereferences    ) {
        this.position = position;
        this.variants = variants;
        this.attributeas = attributeas;
        this.operationmodereferences = operationmodereferences;
    }

    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public Signal getSignal() {
        return signal;
    }

    public void setSignal(Signal signal) {
        this.signal = signal;
    }
    public List<Variant> getVariants() {
        return variants;
    }

    public void addVariant(Variant variant) {
        this.variants.add(variant);
    }
    public DataTypeA getDatatypea() {
        return datatypea;
    }

    public void setDatatypea(DataTypeA datatypea) {
        this.datatypea = datatypea;
    }
    public SignalInMessageCapability getSignalinmessagecapability() {
        return signalinmessagecapability;
    }

    public void setSignalinmessagecapability(SignalInMessageCapability signalinmessagecapability) {
        this.signalinmessagecapability = signalinmessagecapability;
    }
    public List<AttributeA> getAttributeas() {
        return attributeas;
    }

    public void addAttributea(Attributea attributea) {
        this.attributeas.add(attributea);
    }
    public List<OperationModeReference> getOperationmodereferences() {
        return operationmodereferences;
    }

    public void addOperationmodereference(Operationmodereference operationmodereference) {
        this.operationmodereferences.add(operationmodereference);
    }

}