





import java.util.List;
import java.util.ArrayList;

public class PiServiceComposition_Variable  {

    private String name;
    private String type;





    private PiServiceComposition_Policy piservicecomposition_policy;




    private PiServiceComposition_CompositionServiceModel piservicecomposition_compositionservicemodel;


    public PiServiceComposition_Variable(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public PiServiceComposition_Policy getPiservicecomposition_policy() {
        return piservicecomposition_policy;
    }

    public void setPiservicecomposition_policy(PiServiceComposition_Policy piservicecomposition_policy) {
        this.piservicecomposition_policy = piservicecomposition_policy;
    }
    public PiServiceComposition_CompositionServiceModel getPiservicecomposition_compositionservicemodel() {
        return piservicecomposition_compositionservicemodel;
    }

    public void setPiservicecomposition_compositionservicemodel(PiServiceComposition_CompositionServiceModel piservicecomposition_compositionservicemodel) {
        this.piservicecomposition_compositionservicemodel = piservicecomposition_compositionservicemodel;
    }

}