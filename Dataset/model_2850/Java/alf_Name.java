





import java.util.List;
import java.util.ArrayList;

public class alf_Name  {

    private String id;





    private alf_TaggedValue alf_taggedvalue;




    private alf_ImportReference alf_importreference;


    public alf_Name(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public alf_TaggedValue getAlf_taggedvalue() {
        return alf_taggedvalue;
    }

    public void setAlf_taggedvalue(alf_TaggedValue alf_taggedvalue) {
        this.alf_taggedvalue = alf_taggedvalue;
    }
    public alf_ImportReference getAlf_importreference() {
        return alf_importreference;
    }

    public void setAlf_importreference(alf_ImportReference alf_importreference) {
        this.alf_importreference = alf_importreference;
    }

}