





import java.util.List;
import java.util.ArrayList;

public class r1_As extends UnaryExpression {

    private String strict;
    private String asType;



    public r1_As(
        String strict,        String asType    ) {
        super(
        );
        this.strict = strict;
        this.asType = asType;
    }


    public String getStrict() {
        return strict;
    }

    public void setStrict(String strict) {
        this.strict = strict;
    }
    public String getAstype() {
        return asType;
    }

    public void setAstype(String asType) {
        this.asType = asType;
    }


}