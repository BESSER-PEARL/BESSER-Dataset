





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlDataTypeFacet  {

    private String values;
    private String minlen;
    private String maxlen;
    private boolean maxInclusive;
    private String regex;
    private String max;
    private String len;
    private String min;
    private boolean minInclusive;





    private sADL_SadlClassOrPropertyDeclaration sadl_sadlclassorpropertydeclaration;


    public sADL_SadlDataTypeFacet(
        String values,        String minlen,        String maxlen,        boolean maxInclusive,        String regex,        String max,        String len,        String min,        boolean minInclusive    ) {
        this.values = values;
        this.minlen = minlen;
        this.maxlen = maxlen;
        this.maxInclusive = maxInclusive;
        this.regex = regex;
        this.max = max;
        this.len = len;
        this.min = min;
        this.minInclusive = minInclusive;
    }


    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }
    public String getMinlen() {
        return minlen;
    }

    public void setMinlen(String minlen) {
        this.minlen = minlen;
    }
    public String getMaxlen() {
        return maxlen;
    }

    public void setMaxlen(String maxlen) {
        this.maxlen = maxlen;
    }
    public boolean getMaxinclusive() {
        return maxInclusive;
    }

    public void setMaxinclusive(boolean maxInclusive) {
        this.maxInclusive = maxInclusive;
    }
    public String getRegex() {
        return regex;
    }

    public void setRegex(String regex) {
        this.regex = regex;
    }
    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public String getLen() {
        return len;
    }

    public void setLen(String len) {
        this.len = len;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }
    public boolean getMininclusive() {
        return minInclusive;
    }

    public void setMininclusive(boolean minInclusive) {
        this.minInclusive = minInclusive;
    }

    public sADL_SadlClassOrPropertyDeclaration getSadl_sadlclassorpropertydeclaration() {
        return sadl_sadlclassorpropertydeclaration;
    }

    public void setSadl_sadlclassorpropertydeclaration(sADL_SadlClassOrPropertyDeclaration sadl_sadlclassorpropertydeclaration) {
        this.sadl_sadlclassorpropertydeclaration = sadl_sadlclassorpropertydeclaration;
    }

}