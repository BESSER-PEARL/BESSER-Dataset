





import java.util.List;
import java.util.ArrayList;

public class domainmodel_SetRestCallReceiverParameters  {






    private List<domainmodel_SetRestCallReceiverParameter> domainmodel_setrestcallreceiverparameters;


    public domainmodel_SetRestCallReceiverParameters(
    ) {
        this.domainmodel_setrestcallreceiverparameters = new ArrayList<>();
    }

    public domainmodel_SetRestCallReceiverParameters(
        ArrayList<domainmodel_SetRestCallReceiverParameter> domainmodel_setrestcallreceiverparameters    ) {
        this.domainmodel_setrestcallreceiverparameters = domainmodel_setrestcallreceiverparameters;
    }


    public List<domainmodel_SetRestCallReceiverParameter> getDomainmodel_setrestcallreceiverparameters() {
        return domainmodel_setrestcallreceiverparameters;
    }

    public void addDomainmodel_setrestcallreceiverparameter(Domainmodel_setrestcallreceiverparameter domainmodel_setrestcallreceiverparameter) {
        this.domainmodel_setrestcallreceiverparameters.add(domainmodel_setrestcallreceiverparameter);
    }

}