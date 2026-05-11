





import java.util.List;
import java.util.ArrayList;

public class camel_provider_Functional extends Requires {

    private int order;
    private int value;
    private String type;



    public camel_provider_Functional(
        int order,        int value,        String type    ) {
        super(
        );
        this.order = order;
        this.value = value;
        this.type = type;
    }


    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}