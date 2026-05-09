





import java.util.List;
import java.util.ArrayList;

public class syswb101_Thing extends NamedElement {

    private int id;





    private syswb101_Workbench syswb101_workbench;


    public syswb101_Thing(
        int id    ) {
        super(
        );
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public syswb101_Workbench getSyswb101_workbench() {
        return syswb101_workbench;
    }

    public void setSyswb101_workbench(syswb101_Workbench syswb101_workbench) {
        this.syswb101_workbench = syswb101_workbench;
    }

}