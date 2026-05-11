





import java.util.List;
import java.util.ArrayList;

public class behaviour_EntityPrimive extends PrimitiveExpression {

    private String primitive;



    public behaviour_EntityPrimive(
        String primitive    ) {
        super(
        );
        this.primitive = primitive;
    }


    public String getPrimitive() {
        return primitive;
    }

    public void setPrimitive(String primitive) {
        this.primitive = primitive;
    }


}