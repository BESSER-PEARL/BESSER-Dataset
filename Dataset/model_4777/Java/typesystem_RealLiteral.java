





import java.util.List;
import java.util.ArrayList;

public class typesystem_RealLiteral extends NumericLiteral {

    private String data;
    private float value;



    public typesystem_RealLiteral(
        String data,        float value    ) {
        super(
        );
        this.data = data;
        this.value = value;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }


}