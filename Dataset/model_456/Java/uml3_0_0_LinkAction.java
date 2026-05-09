





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_LinkAction extends Action {






    private List<uml3_0_0_LinkEndData> uml3_0_0_linkenddatas;


    public uml3_0_0_LinkAction(
    ) {
        super(
        );
        this.uml3_0_0_linkenddatas = new ArrayList<>();
    }

    public uml3_0_0_LinkAction(
        ArrayList<uml3_0_0_LinkEndData> uml3_0_0_linkenddatas    ) {
        this.uml3_0_0_linkenddatas = uml3_0_0_linkenddatas;
    }


    public List<uml3_0_0_LinkEndData> getUml3_0_0_linkenddatas() {
        return uml3_0_0_linkenddatas;
    }

    public void addUml3_0_0_linkenddata(Uml3_0_0_linkenddata uml3_0_0_linkenddata) {
        this.uml3_0_0_linkenddatas.add(uml3_0_0_linkenddata);
    }

}