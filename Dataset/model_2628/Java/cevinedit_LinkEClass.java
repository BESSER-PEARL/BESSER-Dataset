





import java.util.List;
import java.util.ArrayList;

public class cevinedit_LinkEClass extends Link, PersonalizedElement {

    private String target;
    private String source;



    public cevinedit_LinkEClass(
        String target,        String source    ) {
        super(
        );
        this.target = target;
        this.source = source;
    }


    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }


}