





import java.util.List;
import java.util.ArrayList;

public class raspirover_VarRef extends Statement, StringValue, NumberValue, BooleanValue {

    private float name;



    public raspirover_VarRef(
        float name    ) {
        super(
        );
        this.name = name;
    }


    public float getName() {
        return name;
    }

    public void setName(float name) {
        this.name = name;
    }


}