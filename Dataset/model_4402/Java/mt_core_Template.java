





import java.util.List;
import java.util.ArrayList;

public class mt_core_Template extends Resource {

    private String endTag;
    private String beginTag;



    public mt_core_Template(
        String endTag,        String beginTag    ) {
        super(
        );
        this.endTag = endTag;
        this.beginTag = beginTag;
    }


    public String getEndtag() {
        return endTag;
    }

    public void setEndtag(String endTag) {
        this.endTag = endTag;
    }
    public String getBegintag() {
        return beginTag;
    }

    public void setBegintag(String beginTag) {
        this.beginTag = beginTag;
    }


}