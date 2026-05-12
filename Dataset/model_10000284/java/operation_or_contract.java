





import java.util.List;
import java.util.ArrayList;

public class operation_or_contract  {

    private int operation_id;
    private String customer_id;
    private String owner_id;
    private int Property_id;
    private String operation_type;





    private Property property;




    private owner owner;


    public operation_or_contract(
        int operation_id,        String customer_id,        String owner_id,        int Property_id,        String operation_type    ) {
        this.operation_id = operation_id;
        this.customer_id = customer_id;
        this.owner_id = owner_id;
        this.Property_id = Property_id;
        this.operation_type = operation_type;
    }


    public int getOperation_id() {
        return operation_id;
    }

    public void setOperation_id(int operation_id) {
        this.operation_id = operation_id;
    }
    public String getCustomer_id() {
        return customer_id;
    }

    public void setCustomer_id(String customer_id) {
        this.customer_id = customer_id;
    }
    public String getOwner_id() {
        return owner_id;
    }

    public void setOwner_id(String owner_id) {
        this.owner_id = owner_id;
    }
    public int getProperty_id() {
        return Property_id;
    }

    public void setProperty_id(int Property_id) {
        this.Property_id = Property_id;
    }
    public String getOperation_type() {
        return operation_type;
    }

    public void setOperation_type(String operation_type) {
        this.operation_type = operation_type;
    }

    public Property getProperty() {
        return property;
    }

    public void setProperty(Property property) {
        this.property = property;
    }
    public owner getOwner() {
        return owner;
    }

    public void setOwner(owner owner) {
        this.owner = owner;
    }

}