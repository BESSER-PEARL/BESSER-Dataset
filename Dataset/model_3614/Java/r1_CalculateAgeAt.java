





import java.util.List;
import java.util.ArrayList;

public class r1_CalculateAgeAt extends BinaryExpression {

    private String precision;



    public r1_CalculateAgeAt(
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