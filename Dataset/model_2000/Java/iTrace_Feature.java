





import java.util.List;
import java.util.ArrayList;

public class iTrace_Feature  {

    private String attribute;
    private String value;





    private iTrace_SpecificFeature itrace_specificfeature;




    private iTrace_SpecificFeature itrace_specificfeature;


    public iTrace_Feature(
        String attribute,        String value    ) {
        this.attribute = attribute;
        this.value = value;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public iTrace_SpecificFeature getItrace_specificfeature() {
        return itrace_specificfeature;
    }

    public void setItrace_specificfeature(iTrace_SpecificFeature itrace_specificfeature) {
        this.itrace_specificfeature = itrace_specificfeature;
    }
    public iTrace_SpecificFeature getItrace_specificfeature() {
        return itrace_specificfeature;
    }

    public void setItrace_specificfeature(iTrace_SpecificFeature itrace_specificfeature) {
        this.itrace_specificfeature = itrace_specificfeature;
    }

}