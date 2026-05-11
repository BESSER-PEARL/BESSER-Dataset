





import java.util.List;
import java.util.ArrayList;

public class xal_PremiseNumberSuffix  {

    private String type;
    private String anyAttribute;
    private String code;
    private String mixed;
    private String numberSuffixSeparator;





    private xal_PremiseNumberRangeFrom xal_premisenumberrangefrom;




    private xal_Premise xal_premise;




    private xal_PremiseNumberRangeTo xal_premisenumberrangeto;




    private xal_DocumentRoot xal_documentroot;


    public xal_PremiseNumberSuffix(
        String type,        String anyAttribute,        String code,        String mixed,        String numberSuffixSeparator    ) {
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.code = code;
        this.mixed = mixed;
        this.numberSuffixSeparator = numberSuffixSeparator;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getNumbersuffixseparator() {
        return numberSuffixSeparator;
    }

    public void setNumbersuffixseparator(String numberSuffixSeparator) {
        this.numberSuffixSeparator = numberSuffixSeparator;
    }

    public xal_PremiseNumberRangeFrom getXal_premisenumberrangefrom() {
        return xal_premisenumberrangefrom;
    }

    public void setXal_premisenumberrangefrom(xal_PremiseNumberRangeFrom xal_premisenumberrangefrom) {
        this.xal_premisenumberrangefrom = xal_premisenumberrangefrom;
    }
    public xal_Premise getXal_premise() {
        return xal_premise;
    }

    public void setXal_premise(xal_Premise xal_premise) {
        this.xal_premise = xal_premise;
    }
    public xal_PremiseNumberRangeTo getXal_premisenumberrangeto() {
        return xal_premisenumberrangeto;
    }

    public void setXal_premisenumberrangeto(xal_PremiseNumberRangeTo xal_premisenumberrangeto) {
        this.xal_premisenumberrangeto = xal_premisenumberrangeto;
    }
    public xal_DocumentRoot getXal_documentroot() {
        return xal_documentroot;
    }

    public void setXal_documentroot(xal_DocumentRoot xal_documentroot) {
        this.xal_documentroot = xal_documentroot;
    }

}