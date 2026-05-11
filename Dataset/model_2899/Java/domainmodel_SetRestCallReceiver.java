





import java.util.List;
import java.util.ArrayList;

public class domainmodel_SetRestCallReceiver extends SetActionReceiver {






    private List<domainmodel_SetRestCallReceiverParameters> domainmodel_setrestcallreceiverparameterss;


    public domainmodel_SetRestCallReceiver(
    ) {
        super(
        );
        this.domainmodel_setrestcallreceiverparameterss = new ArrayList<>();
    }

    public domainmodel_SetRestCallReceiver(
        ArrayList<domainmodel_SetRestCallReceiverParameters> domainmodel_setrestcallreceiverparameterss    ) {
        this.domainmodel_setrestcallreceiverparameterss = domainmodel_setrestcallreceiverparameterss;
    }


    public List<domainmodel_SetRestCallReceiverParameters> getDomainmodel_setrestcallreceiverparameterss() {
        return domainmodel_setrestcallreceiverparameterss;
    }

    public void addDomainmodel_setrestcallreceiverparameters(Domainmodel_setrestcallreceiverparameters domainmodel_setrestcallreceiverparameters) {
        this.domainmodel_setrestcallreceiverparameterss.add(domainmodel_setrestcallreceiverparameters);
    }

}