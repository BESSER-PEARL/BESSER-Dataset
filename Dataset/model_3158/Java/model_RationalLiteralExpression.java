





import java.util.List;
import java.util.ArrayList;

public class model_RationalLiteralExpression extends ArithmeticLiteralExpression {

    private String numerator;
    private String denominator;



    public model_RationalLiteralExpression(
        String numerator,        String denominator    ) {
        super(
        );
        this.numerator = numerator;
        this.denominator = denominator;
    }


    public String getNumerator() {
        return numerator;
    }

    public void setNumerator(String numerator) {
        this.numerator = numerator;
    }
    public String getDenominator() {
        return denominator;
    }

    public void setDenominator(String denominator) {
        this.denominator = denominator;
    }


}