





import java.util.List;
import java.util.ArrayList;

public class xal_PremiseNumber  {

    private String indicatorOccurrence;
    private String type;
    private String indicator;
    private String numberType;
    private String mixed;
    private String code;
    private String anyAttribute;
    private String numberTypeOccurrence;





    private xal_PremiseNumberRangeTo xal_premisenumberrangeto;




    private xal_Premise xal_premise;




    private xal_DocumentRoot xal_documentroot;




    private xal_PremiseNumberRangeFrom xal_premisenumberrangefrom;


    public xal_PremiseNumber(
        String indicatorOccurrence,        String type,        String indicator,        String numberType,        String mixed,        String code,        String anyAttribute,        String numberTypeOccurrence    ) {
        this.indicatorOccurrence = indicatorOccurrence;
        this.type = type;
        this.indicator = indicator;
        this.numberType = numberType;
        this.mixed = mixed;
        this.code = code;
        this.anyAttribute = anyAttribute;
        this.numberTypeOccurrence = numberTypeOccurrence;
    }


    public String getIndicatoroccurrence() {
        return indicatorOccurrence;
    }

    public void setIndicatoroccurrence(String indicatorOccurrence) {
        this.indicatorOccurrence = indicatorOccurrence;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getIndicator() {
        return indicator;
    }

    public void setIndicator(String indicator) {
        this.indicator = indicator;
    }
    public String getNumbertype() {
        return numberType;
    }

    public void setNumbertype(String numberType) {
        this.numberType = numberType;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getNumbertypeoccurrence() {
        return numberTypeOccurrence;
    }

    public void setNumbertypeoccurrence(String numberTypeOccurrence) {
        this.numberTypeOccurrence = numberTypeOccurrence;
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
    public xal_DocumentRoot getXal_documentroot() {
        return xal_documentroot;
    }

    public void setXal_documentroot(xal_DocumentRoot xal_documentroot) {
        this.xal_documentroot = xal_documentroot;
    }
    public xal_PremiseNumberRangeFrom getXal_premisenumberrangefrom() {
        return xal_premisenumberrangefrom;
    }

    public void setXal_premisenumberrangefrom(xal_PremiseNumberRangeFrom xal_premisenumberrangefrom) {
        this.xal_premisenumberrangefrom = xal_premisenumberrangefrom;
    }

}