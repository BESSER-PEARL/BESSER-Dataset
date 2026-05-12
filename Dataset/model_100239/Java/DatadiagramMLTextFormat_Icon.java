





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLTextFormat_Icon extends MasterElt {

    private String value;





    private MasterShortCut mastershortcut;


    public DatadiagramMLTextFormat_Icon(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public MasterShortCut getMastershortcut() {
        return mastershortcut;
    }

    public void setMastershortcut(MasterShortCut mastershortcut) {
        this.mastershortcut = mastershortcut;
    }

}