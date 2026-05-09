





import java.util.List;
import java.util.ArrayList;

public class pivot_DataType extends Class {

    private String isSerializable;





    private pivot_Type pivot_type;


    public pivot_DataType(
        String isSerializable    ) {
        super(
        );
        this.isSerializable = isSerializable;
    }


    public String getIsserializable() {
        return isSerializable;
    }

    public void setIsserializable(String isSerializable) {
        this.isSerializable = isSerializable;
    }

    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }

}