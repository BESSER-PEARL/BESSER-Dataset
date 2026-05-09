





import java.util.List;
import java.util.ArrayList;

public class PHPMVC_extPHP_Anchor extends HTMLElement {

    private String content;
    private String target;
    private String hypRef;



    public PHPMVC_extPHP_Anchor(
        String content,        String target,        String hypRef    ) {
        super(
        );
        this.content = content;
        this.target = target;
        this.hypRef = hypRef;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getHypref() {
        return hypRef;
    }

    public void setHypref(String hypRef) {
        this.hypRef = hypRef;
    }


}