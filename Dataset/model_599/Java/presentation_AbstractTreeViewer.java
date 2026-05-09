





import java.util.List;
import java.util.ArrayList;

public class presentation_AbstractTreeViewer extends ColumnViewer {

    private String group4;
    private String autoExpandLevel;



    public presentation_AbstractTreeViewer(
        String group4,        String autoExpandLevel    ) {
        super(
        );
        this.group4 = group4;
        this.autoExpandLevel = autoExpandLevel;
    }


    public String getGroup4() {
        return group4;
    }

    public void setGroup4(String group4) {
        this.group4 = group4;
    }
    public String getAutoexpandlevel() {
        return autoExpandLevel;
    }

    public void setAutoexpandlevel(String autoExpandLevel) {
        this.autoExpandLevel = autoExpandLevel;
    }


}