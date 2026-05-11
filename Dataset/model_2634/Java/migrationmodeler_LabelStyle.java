





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_LabelStyle extends BasicLabelStyle {

    private String labelAlignment;



    public migrationmodeler_LabelStyle(
        String labelAlignment    ) {
        super(
        );
        this.labelAlignment = labelAlignment;
    }


    public String getLabelalignment() {
        return labelAlignment;
    }

    public void setLabelalignment(String labelAlignment) {
        this.labelAlignment = labelAlignment;
    }


}