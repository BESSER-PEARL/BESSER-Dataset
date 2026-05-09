





import java.util.List;
import java.util.ArrayList;

public class syswb101_Thoughts extends NamedElement {






    private List<syswb101_Thing> syswb101_things;




    private syswb101_Workbench syswb101_workbench;


    public syswb101_Thoughts(
    ) {
        super(
        );
        this.syswb101_things = new ArrayList<>();
    }

    public syswb101_Thoughts(
        ArrayList<syswb101_Thing> syswb101_things    ) {
        this.syswb101_things = syswb101_things;
    }


    public List<syswb101_Thing> getSyswb101_things() {
        return syswb101_things;
    }

    public void addSyswb101_thing(Syswb101_thing syswb101_thing) {
        this.syswb101_things.add(syswb101_thing);
    }
    public syswb101_Workbench getSyswb101_workbench() {
        return syswb101_workbench;
    }

    public void setSyswb101_workbench(syswb101_Workbench syswb101_workbench) {
        this.syswb101_workbench = syswb101_workbench;
    }

}