





import java.util.List;
import java.util.ArrayList;

public class uml_LinkAction extends Action {






    private List<uml_LinkEndData> uml_linkenddatas;


    public uml_LinkAction(
    ) {
        super(
        );
        this.uml_linkenddatas = new ArrayList<>();
    }

    public uml_LinkAction(
        ArrayList<uml_LinkEndData> uml_linkenddatas    ) {
        this.uml_linkenddatas = uml_linkenddatas;
    }


    public List<uml_LinkEndData> getUml_linkenddatas() {
        return uml_linkenddatas;
    }

    public void addUml_linkenddata(Uml_linkenddata uml_linkenddata) {
        this.uml_linkenddatas.add(uml_linkenddata);
    }

}