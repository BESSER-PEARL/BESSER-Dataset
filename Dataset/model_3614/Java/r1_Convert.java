





import java.util.List;
import java.util.ArrayList;

public class r1_Convert extends UnaryExpression {

    private String toType;



    public r1_Convert(
        String toType    ) {
        super(
        );
        this.toType = toType;
    }


    public String getTotype() {
        return toType;
    }

    public void setTotype(String toType) {
        this.toType = toType;
    }


}