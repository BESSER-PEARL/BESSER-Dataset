





import java.util.List;
import java.util.ArrayList;

public class Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo  {

    private String additionalServiceName;
    private String additionalServicePrice;





    private Implementation_DecisionSupportComponent_BookingDSSInfo implementation_decisionsupportcomponent_bookingdssinfo;




    private Implementation_DecisionSupportComponent_DSSController implementation_decisionsupportcomponent_dsscontroller;


    public Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo(
        String additionalServiceName,        String additionalServicePrice    ) {
        this.additionalServiceName = additionalServiceName;
        this.additionalServicePrice = additionalServicePrice;
    }


    public String getAdditionalservicename() {
        return additionalServiceName;
    }

    public void setAdditionalservicename(String additionalServiceName) {
        this.additionalServiceName = additionalServiceName;
    }
    public String getAdditionalserviceprice() {
        return additionalServicePrice;
    }

    public void setAdditionalserviceprice(String additionalServicePrice) {
        this.additionalServicePrice = additionalServicePrice;
    }

    public Implementation_DecisionSupportComponent_BookingDSSInfo getImplementation_decisionsupportcomponent_bookingdssinfo() {
        return implementation_decisionsupportcomponent_bookingdssinfo;
    }

    public void setImplementation_decisionsupportcomponent_bookingdssinfo(Implementation_DecisionSupportComponent_BookingDSSInfo implementation_decisionsupportcomponent_bookingdssinfo) {
        this.implementation_decisionsupportcomponent_bookingdssinfo = implementation_decisionsupportcomponent_bookingdssinfo;
    }
    public Implementation_DecisionSupportComponent_DSSController getImplementation_decisionsupportcomponent_dsscontroller() {
        return implementation_decisionsupportcomponent_dsscontroller;
    }

    public void setImplementation_decisionsupportcomponent_dsscontroller(Implementation_DecisionSupportComponent_DSSController implementation_decisionsupportcomponent_dsscontroller) {
        this.implementation_decisionsupportcomponent_dsscontroller = implementation_decisionsupportcomponent_dsscontroller;
    }

}