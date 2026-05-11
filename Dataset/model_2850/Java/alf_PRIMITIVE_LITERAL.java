





import java.util.List;
import java.util.ArrayList;

public class alf_PRIMITIVE_LITERAL  {

    private String value;





    private alf_TaggedValue alf_taggedvalue;


    public alf_PRIMITIVE_LITERAL(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public alf_TaggedValue getAlf_taggedvalue() {
        return alf_taggedvalue;
    }

    public void setAlf_taggedvalue(alf_TaggedValue alf_taggedvalue) {
        this.alf_taggedvalue = alf_taggedvalue;
    }

}