





import java.util.List;
import java.util.ArrayList;

public class sadl_Facets  {

    private String max;
    private String len;
    private String min;
    private String maxlen;
    private String minexin;
    private String maxexin;
    private String values;
    private String regex;
    private String minlen;





    private sadl_DataTypeRestriction sadl_datatyperestriction;


    public sadl_Facets(
        String max,        String len,        String min,        String maxlen,        String minexin,        String maxexin,        String values,        String regex,        String minlen    ) {
        this.max = max;
        this.len = len;
        this.min = min;
        this.maxlen = maxlen;
        this.minexin = minexin;
        this.maxexin = maxexin;
        this.values = values;
        this.regex = regex;
        this.minlen = minlen;
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
    public String getMaxlen() {
        return maxlen;
    }

    public void setMaxlen(String maxlen) {
        this.maxlen = maxlen;
    }
    public String getMinexin() {
        return minexin;
    }

    public void setMinexin(String minexin) {
        this.minexin = minexin;
    }
    public String getMaxexin() {
        return maxexin;
    }

    public void setMaxexin(String maxexin) {
        this.maxexin = maxexin;
    }
    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }
    public String getRegex() {
        return regex;
    }

    public void setRegex(String regex) {
        this.regex = regex;
    }
    public String getMinlen() {
        return minlen;
    }

    public void setMinlen(String minlen) {
        this.minlen = minlen;
    }

    public sadl_DataTypeRestriction getSadl_datatyperestriction() {
        return sadl_datatyperestriction;
    }

    public void setSadl_datatyperestriction(sadl_DataTypeRestriction sadl_datatyperestriction) {
        this.sadl_datatyperestriction = sadl_datatyperestriction;
    }

}