





import java.util.List;
import java.util.ArrayList;

public class r1_SameOrBefore extends BinaryExpression {

    private String precision;



    public r1_SameOrBefore(
        String precision    ) {
        super(
        );
        this.precision = precision;
    }


    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
    }


}