





import java.util.List;
import java.util.ArrayList;

public class delphi_statement extends CSTrace {

    private String labelId;



    public delphi_statement(
        String labelId    ) {
        super(
        );
        this.labelId = labelId;
    }


    public String getLabelid() {
        return labelId;
    }

    public void setLabelid(String labelId) {
        this.labelId = labelId;
    }


}