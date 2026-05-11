





import java.util.List;
import java.util.ArrayList;

public class simulink_Goto extends VirtualBlock {

    private String gotoTag;
    private String tagVisibility;



    public simulink_Goto(
        String gotoTag,        String tagVisibility    ) {
        super(
        );
        this.gotoTag = gotoTag;
        this.tagVisibility = tagVisibility;
    }


    public String getGototag() {
        return gotoTag;
    }

    public void setGototag(String gotoTag) {
        this.gotoTag = gotoTag;
    }
    public String getTagvisibility() {
        return tagVisibility;
    }

    public void setTagvisibility(String tagVisibility) {
        this.tagVisibility = tagVisibility;
    }


}