





import java.util.List;
import java.util.ArrayList;

public class domainDsl_Validator  {

    private String svalue;
    private String name;
    private int value;





    private domainDsl_Feature domaindsl_feature;


    public domainDsl_Validator(
        String svalue,        String name,        int value    ) {
        this.svalue = svalue;
        this.name = name;
        this.value = value;
    }


    public String getSvalue() {
        return svalue;
    }

    public void setSvalue(String svalue) {
        this.svalue = svalue;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public domainDsl_Feature getDomaindsl_feature() {
        return domaindsl_feature;
    }

    public void setDomaindsl_feature(domainDsl_Feature domaindsl_feature) {
        this.domaindsl_feature = domaindsl_feature;
    }

}