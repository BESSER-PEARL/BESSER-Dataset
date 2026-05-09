





import java.util.List;
import java.util.ArrayList;

public class presentation_ExpandBar extends Composite {

    private String spacing;
    private String group3;



    public presentation_ExpandBar(
        String spacing,        String group3    ) {
        super(
        );
        this.spacing = spacing;
        this.group3 = group3;
    }


    public String getSpacing() {
        return spacing;
    }

    public void setSpacing(String spacing) {
        this.spacing = spacing;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }


}