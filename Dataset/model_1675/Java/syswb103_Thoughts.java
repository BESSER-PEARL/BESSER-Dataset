





import java.util.List;
import java.util.ArrayList;

public class syswb103_Thoughts extends NamedElement {






    private syswb103_Workbench syswb103_workbench;




    private List<syswb103_Thing> syswb103_things;


    public syswb103_Thoughts(
    ) {
        super(
        );
        this.syswb103_things = new ArrayList<>();
    }

    public syswb103_Thoughts(
        ArrayList<syswb103_Thing> syswb103_things    ) {
        this.syswb103_things = syswb103_things;
    }


    public syswb103_Workbench getSyswb103_workbench() {
        return syswb103_workbench;
    }

    public void setSyswb103_workbench(syswb103_Workbench syswb103_workbench) {
        this.syswb103_workbench = syswb103_workbench;
    }
    public List<syswb103_Thing> getSyswb103_things() {
        return syswb103_things;
    }

    public void addSyswb103_thing(Syswb103_thing syswb103_thing) {
        this.syswb103_things.add(syswb103_thing);
    }

}