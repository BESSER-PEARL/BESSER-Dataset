





import java.util.List;
import java.util.ArrayList;

public class r1_As extends UnaryExpression {

    private String asType;
    private String strict;



    public r1_As(
        String asType,        String strict    ) {
        super(
        );
        this.asType = asType;
        this.strict = strict;
    }


    public String getAstype() {
        return asType;
    }

    public void setAstype(String asType) {
        this.asType = asType;
    }
    public String getStrict() {
        return strict;
    }

    public void setStrict(String strict) {
        this.strict = strict;
    }


}