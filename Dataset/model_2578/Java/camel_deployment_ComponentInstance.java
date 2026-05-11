




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class camel_deployment_ComponentInstance extends DeploymentElement {

    private LocalDate destroyedOn;
    private LocalDate instantiatedOn;



    public camel_deployment_ComponentInstance(
        LocalDate destroyedOn,        LocalDate instantiatedOn    ) {
        super(
        );
        this.destroyedOn = destroyedOn;
        this.instantiatedOn = instantiatedOn;
    }


    public LocalDate getDestroyedon() {
        return destroyedOn;
    }

    public void setDestroyedon(LocalDate destroyedOn) {
        this.destroyedOn = destroyedOn;
    }
    public LocalDate getInstantiatedon() {
        return instantiatedOn;
    }

    public void setInstantiatedon(LocalDate instantiatedOn) {
        this.instantiatedOn = instantiatedOn;
    }


}