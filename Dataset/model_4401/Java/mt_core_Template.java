





import java.util.List;
import java.util.ArrayList;

public class mt_core_Template extends Resource {

    private String beginTag;
    private String endTag;



    public mt_core_Template(
        String beginTag,        String endTag    ) {
        super(
        );
        this.beginTag = beginTag;
        this.endTag = endTag;
    }


    public String getBegintag() {
        return beginTag;
    }

    public void setBegintag(String beginTag) {
        this.beginTag = beginTag;
    }
    public String getEndtag() {
        return endTag;
    }

    public void setEndtag(String endTag) {
        this.endTag = endTag;
    }


}