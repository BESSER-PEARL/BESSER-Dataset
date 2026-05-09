





import java.util.List;
import java.util.ArrayList;

public class eTJ_RealFormat extends NumberFormat, CurrencyFormat {

    private String thousandsSeparator;
    private String fractionSeparator;
    private String negativePrefix;
    private int fractionDigits;
    private String negativeSuffix;



    public eTJ_RealFormat(
        String thousandsSeparator,        String fractionSeparator,        String negativePrefix,        int fractionDigits,        String negativeSuffix    ) {
        super(
        );
        this.thousandsSeparator = thousandsSeparator;
        this.fractionSeparator = fractionSeparator;
        this.negativePrefix = negativePrefix;
        this.fractionDigits = fractionDigits;
        this.negativeSuffix = negativeSuffix;
    }


    public String getThousandsseparator() {
        return thousandsSeparator;
    }

    public void setThousandsseparator(String thousandsSeparator) {
        this.thousandsSeparator = thousandsSeparator;
    }
    public String getFractionseparator() {
        return fractionSeparator;
    }

    public void setFractionseparator(String fractionSeparator) {
        this.fractionSeparator = fractionSeparator;
    }
    public String getNegativeprefix() {
        return negativePrefix;
    }

    public void setNegativeprefix(String negativePrefix) {
        this.negativePrefix = negativePrefix;
    }
    public int getFractiondigits() {
        return fractionDigits;
    }

    public void setFractiondigits(int fractionDigits) {
        this.fractionDigits = fractionDigits;
    }
    public String getNegativesuffix() {
        return negativeSuffix;
    }

    public void setNegativesuffix(String negativeSuffix) {
        this.negativeSuffix = negativeSuffix;
    }


}