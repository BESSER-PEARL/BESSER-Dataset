





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_ModifyRelationship  {

    private String targetParameterName;
    private String name;
    private String function;
    private int orderNumber;





    private servicefeaturemodel_Attribute servicefeaturemodel_attribute;


    public servicefeaturemodel_ModifyRelationship(
        String targetParameterName,        String name,        String function,        int orderNumber    ) {
        this.targetParameterName = targetParameterName;
        this.name = name;
        this.function = function;
        this.orderNumber = orderNumber;
    }


    public String getTargetparametername() {
        return targetParameterName;
    }

    public void setTargetparametername(String targetParameterName) {
        this.targetParameterName = targetParameterName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }
    public int getOrdernumber() {
        return orderNumber;
    }

    public void setOrdernumber(int orderNumber) {
        this.orderNumber = orderNumber;
    }

    public servicefeaturemodel_Attribute getServicefeaturemodel_attribute() {
        return servicefeaturemodel_attribute;
    }

    public void setServicefeaturemodel_attribute(servicefeaturemodel_Attribute servicefeaturemodel_attribute) {
        this.servicefeaturemodel_attribute = servicefeaturemodel_attribute;
    }

}