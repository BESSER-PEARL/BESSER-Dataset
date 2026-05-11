





import java.util.List;
import java.util.ArrayList;

public class TTMCConstraint_RationalLiteralExpression extends ArithmeticLiteralExpression {

    private String denominator;
    private String numerator;



    public TTMCConstraint_RationalLiteralExpression(
        String denominator,        String numerator    ) {
        super(
        );
        this.denominator = denominator;
        this.numerator = numerator;
    }


    public String getDenominator() {
        return denominator;
    }

    public void setDenominator(String denominator) {
        this.denominator = denominator;
    }
    public String getNumerator() {
        return numerator;
    }

    public void setNumerator(String numerator) {
        this.numerator = numerator;
    }


}