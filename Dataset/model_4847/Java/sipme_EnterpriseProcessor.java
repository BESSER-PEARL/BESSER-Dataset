





import java.util.List;
import java.util.ArrayList;

public class sipme_EnterpriseProcessor extends EnterpriseObject {

    private String processorOrigin;





    private List<sipme_Capacity> sipme_capacitys;




    private List<sipme_Capability> sipme_capabilitys;


    public sipme_EnterpriseProcessor(
        String processorOrigin    ) {
        super(
        );
        this.processorOrigin = processorOrigin;
        this.sipme_capacitys = new ArrayList<>();
        this.sipme_capabilitys = new ArrayList<>();
    }

    public sipme_EnterpriseProcessor(
        String processorOrigin        ArrayList<sipme_Capacity> sipme_capacitys,        ArrayList<sipme_Capability> sipme_capabilitys    ) {
        this.processorOrigin = processorOrigin;
        this.sipme_capacitys = sipme_capacitys;
        this.sipme_capabilitys = sipme_capabilitys;
    }

    public String getProcessororigin() {
        return processorOrigin;
    }

    public void setProcessororigin(String processorOrigin) {
        this.processorOrigin = processorOrigin;
    }

    public List<sipme_Capacity> getSipme_capacitys() {
        return sipme_capacitys;
    }

    public void addSipme_capacity(Sipme_capacity sipme_capacity) {
        this.sipme_capacitys.add(sipme_capacity);
    }
    public List<sipme_Capability> getSipme_capabilitys() {
        return sipme_capabilitys;
    }

    public void addSipme_capability(Sipme_capability sipme_capability) {
        this.sipme_capabilitys.add(sipme_capability);
    }

}