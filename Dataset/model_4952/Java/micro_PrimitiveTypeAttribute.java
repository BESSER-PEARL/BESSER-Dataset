





import java.util.List;
import java.util.ArrayList;

public class micro_PrimitiveTypeAttribute extends Attribute {

    private String type;





    private micro_Model micro_model;


    public micro_PrimitiveTypeAttribute(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public micro_Model getMicro_model() {
        return micro_model;
    }

    public void setMicro_model(micro_Model micro_model) {
        this.micro_model = micro_model;
    }

}