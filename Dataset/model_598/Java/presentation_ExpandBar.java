





import java.util.List;
import java.util.ArrayList;

public class presentation_ExpandBar extends Composite {

    private String group3;
    private String spacing;



    public presentation_ExpandBar(
        String group3,        String spacing    ) {
        super(
        );
        this.group3 = group3;
        this.spacing = spacing;
    }


    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getSpacing() {
        return spacing;
    }

    public void setSpacing(String spacing) {
        this.spacing = spacing;
    }


}