





import java.util.List;
import java.util.ArrayList;

public class langc_Literal extends Expression {

    private String primitiveType;



    public langc_Literal(
        String primitiveType    ) {
        super(
        );
        this.primitiveType = primitiveType;
    }


    public String getPrimitivetype() {
        return primitiveType;
    }

    public void setPrimitivetype(String primitiveType) {
        this.primitiveType = primitiveType;
    }


}