





import java.util.List;
import java.util.ArrayList;

public class xal_PremiseNumberPrefix  {

    private String type;
    private String code;
    private String value;
    private String numberPrefixSeparator;
    private String anyAttribute;





    private xal_PremiseNumberRangeFrom xal_premisenumberrangefrom;




    private xal_DocumentRoot xal_documentroot;




    private xal_PremiseNumberRangeTo xal_premisenumberrangeto;




    private xal_Premise xal_premise;


    public xal_PremiseNumberPrefix(
        String type,        String code,        String value,        String numberPrefixSeparator,        String anyAttribute    ) {
        this.type = type;
        this.code = code;
        this.value = value;
        this.numberPrefixSeparator = numberPrefixSeparator;
        this.anyAttribute = anyAttribute;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getNumberprefixseparator() {
        return numberPrefixSeparator;
    }

    public void setNumberprefixseparator(String numberPrefixSeparator) {
        this.numberPrefixSeparator = numberPrefixSeparator;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }

    public xal_PremiseNumberRangeFrom getXal_premisenumberrangefrom() {
        return xal_premisenumberrangefrom;
    }

    public void setXal_premisenumberrangefrom(xal_PremiseNumberRangeFrom xal_premisenumberrangefrom) {
        this.xal_premisenumberrangefrom = xal_premisenumberrangefrom;
    }
    public xal_DocumentRoot getXal_documentroot() {
        return xal_documentroot;
    }

    public void setXal_documentroot(xal_DocumentRoot xal_documentroot) {
        this.xal_documentroot = xal_documentroot;
    }
    public xal_PremiseNumberRangeTo getXal_premisenumberrangeto() {
        return xal_premisenumberrangeto;
    }

    public void setXal_premisenumberrangeto(xal_PremiseNumberRangeTo xal_premisenumberrangeto) {
        this.xal_premisenumberrangeto = xal_premisenumberrangeto;
    }
    public xal_Premise getXal_premise() {
        return xal_premise;
    }

    public void setXal_premise(xal_Premise xal_premise) {
        this.xal_premise = xal_premise;
    }

}