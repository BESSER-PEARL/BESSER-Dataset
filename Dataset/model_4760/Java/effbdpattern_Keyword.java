





import java.util.List;
import java.util.ArrayList;

public class effbdpattern_Keyword  {

    private String value;





    private effbdpattern_Workbench effbdpattern_workbench;




    private effbdpattern_Indexable effbdpattern_indexable;


    public effbdpattern_Keyword(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public effbdpattern_Workbench getEffbdpattern_workbench() {
        return effbdpattern_workbench;
    }

    public void setEffbdpattern_workbench(effbdpattern_Workbench effbdpattern_workbench) {
        this.effbdpattern_workbench = effbdpattern_workbench;
    }
    public effbdpattern_Indexable getEffbdpattern_indexable() {
        return effbdpattern_indexable;
    }

    public void setEffbdpattern_indexable(effbdpattern_Indexable effbdpattern_indexable) {
        this.effbdpattern_indexable = effbdpattern_indexable;
    }

}