





import java.util.List;
import java.util.ArrayList;

public class lua_Expression_Number extends Expression {

    private float value;



    public lua_Expression_Number(
        float value    ) {
        super(
        );
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }


}