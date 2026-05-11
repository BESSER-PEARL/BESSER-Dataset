





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_ModifyRelationship  {

    private String name;
    private int orderNumber;
    private String targetParameterName;
    private String function;





    private servicefeaturemodel_Attribute servicefeaturemodel_attribute;


    public servicefeaturemodel_ModifyRelationship(
        String name,        int orderNumber,        String targetParameterName,        String function    ) {
        this.name = name;
        this.orderNumber = orderNumber;
        this.targetParameterName = targetParameterName;
        this.function = function;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getOrdernumber() {
        return orderNumber;
    }

    public void setOrdernumber(int orderNumber) {
        this.orderNumber = orderNumber;
    }
    public String getTargetparametername() {
        return targetParameterName;
    }

    public void setTargetparametername(String targetParameterName) {
        this.targetParameterName = targetParameterName;
    }
    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }

    public servicefeaturemodel_Attribute getServicefeaturemodel_attribute() {
        return servicefeaturemodel_attribute;
    }

    public void setServicefeaturemodel_attribute(servicefeaturemodel_Attribute servicefeaturemodel_attribute) {
        this.servicefeaturemodel_attribute = servicefeaturemodel_attribute;
    }

}