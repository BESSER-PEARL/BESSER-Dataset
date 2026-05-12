





import java.util.List;
import java.util.ArrayList;

public class pivot_DataType extends Class {

    private String isSerializable;





    private pivot_Class pivot_class;


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

    public pivot_Class getPivot_class() {
        return pivot_class;
    }

    public void setPivot_class(pivot_Class pivot_class) {
        this.pivot_class = pivot_class;
    }

}