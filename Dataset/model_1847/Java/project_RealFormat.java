





import java.util.List;
import java.util.ArrayList;

public class project_RealFormat extends CurrencyFormat, NumberFormat {

    private String fractionSeparator;
    private String negativePrefix;
    private String thousandsSeparator;
    private String negativeSuffix;
    private int fractionDigits;



    public project_RealFormat(
        String fractionSeparator,        String negativePrefix,        String thousandsSeparator,        String negativeSuffix,        int fractionDigits    ) {
        super(
        );
        this.fractionSeparator = fractionSeparator;
        this.negativePrefix = negativePrefix;
        this.thousandsSeparator = thousandsSeparator;
        this.negativeSuffix = negativeSuffix;
        this.fractionDigits = fractionDigits;
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
    public String getThousandsseparator() {
        return thousandsSeparator;
    }

    public void setThousandsseparator(String thousandsSeparator) {
        this.thousandsSeparator = thousandsSeparator;
    }
    public String getNegativesuffix() {
        return negativeSuffix;
    }

    public void setNegativesuffix(String negativeSuffix) {
        this.negativeSuffix = negativeSuffix;
    }
    public int getFractiondigits() {
        return fractionDigits;
    }

    public void setFractiondigits(int fractionDigits) {
        this.fractionDigits = fractionDigits;
    }


}