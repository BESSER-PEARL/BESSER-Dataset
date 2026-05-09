





import java.util.List;
import java.util.ArrayList;

public class PHPMVC_extPHP_HTMLElement extends ViewComponent {

    private boolean isPairedTag;
    private String tagName;
    private boolean isEmpty;



    public PHPMVC_extPHP_HTMLElement(
        boolean isPairedTag,        String tagName,        boolean isEmpty    ) {
        super(
        );
        this.isPairedTag = isPairedTag;
        this.tagName = tagName;
        this.isEmpty = isEmpty;
    }


    public boolean getIspairedtag() {
        return isPairedTag;
    }

    public void setIspairedtag(boolean isPairedTag) {
        this.isPairedTag = isPairedTag;
    }
    public String getTagname() {
        return tagName;
    }

    public void setTagname(String tagName) {
        this.tagName = tagName;
    }
    public boolean getIsempty() {
        return isEmpty;
    }

    public void setIsempty(boolean isEmpty) {
        this.isEmpty = isEmpty;
    }


}