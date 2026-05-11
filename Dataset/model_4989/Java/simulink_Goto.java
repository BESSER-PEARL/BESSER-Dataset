





import java.util.List;
import java.util.ArrayList;

public class simulink_Goto extends VirtualBlock {

    private String tagVisibility;
    private String gotoTag;



    public simulink_Goto(
        String tagVisibility,        String gotoTag    ) {
        super(
        );
        this.tagVisibility = tagVisibility;
        this.gotoTag = gotoTag;
    }


    public String getTagvisibility() {
        return tagVisibility;
    }

    public void setTagvisibility(String tagVisibility) {
        this.tagVisibility = tagVisibility;
    }
    public String getGototag() {
        return gotoTag;
    }

    public void setGototag(String gotoTag) {
        this.gotoTag = gotoTag;
    }


}