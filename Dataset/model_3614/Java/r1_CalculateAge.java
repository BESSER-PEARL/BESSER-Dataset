





import java.util.List;
import java.util.ArrayList;

public class r1_CalculateAge extends UnaryExpression {

    private String precision;



    public r1_CalculateAge(
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