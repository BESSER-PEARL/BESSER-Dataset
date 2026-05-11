





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_Attribute  {

    private String id;
    private String instantiationValue;





    private servicefeaturemodel_ServiceFeature servicefeaturemodel_servicefeature;


    public servicefeaturemodel_Attribute(
        String id,        String instantiationValue    ) {
        this.id = id;
        this.instantiationValue = instantiationValue;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getInstantiationvalue() {
        return instantiationValue;
    }

    public void setInstantiationvalue(String instantiationValue) {
        this.instantiationValue = instantiationValue;
    }

    public servicefeaturemodel_ServiceFeature getServicefeaturemodel_servicefeature() {
        return servicefeaturemodel_servicefeature;
    }

    public void setServicefeaturemodel_servicefeature(servicefeaturemodel_ServiceFeature servicefeaturemodel_servicefeature) {
        this.servicefeaturemodel_servicefeature = servicefeaturemodel_servicefeature;
    }

}