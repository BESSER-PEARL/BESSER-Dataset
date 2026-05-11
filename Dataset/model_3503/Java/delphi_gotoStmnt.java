





import java.util.List;
import java.util.ArrayList;

public class delphi_gotoStmnt extends simpleStatement {

    private String label;



    public delphi_gotoStmnt(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}