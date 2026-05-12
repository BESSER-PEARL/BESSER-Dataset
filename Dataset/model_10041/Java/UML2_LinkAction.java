





import java.util.List;
import java.util.ArrayList;

public class UML2_LinkAction extends Action {






    private List<UML2_LinkEndData> uml2_linkenddatas;


    public UML2_LinkAction(
    ) {
        super(
        );
        this.uml2_linkenddatas = new ArrayList<>();
    }

    public UML2_LinkAction(
        ArrayList<UML2_LinkEndData> uml2_linkenddatas    ) {
        this.uml2_linkenddatas = uml2_linkenddatas;
    }


    public List<UML2_LinkEndData> getUml2_linkenddatas() {
        return uml2_linkenddatas;
    }

    public void addUml2_linkenddata(Uml2_linkenddata uml2_linkenddata) {
        this.uml2_linkenddatas.add(uml2_linkenddata);
    }

}