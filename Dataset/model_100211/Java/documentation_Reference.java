





import java.util.List;
import java.util.ArrayList;

public class documentation_Reference extends NamedElement, Text {

    private String referredLabel;



    public documentation_Reference(
        String referredLabel    ) {
        super(
        );
        this.referredLabel = referredLabel;
    }


    public String getReferredlabel() {
        return referredLabel;
    }

    public void setReferredlabel(String referredLabel) {
        this.referredLabel = referredLabel;
    }


}