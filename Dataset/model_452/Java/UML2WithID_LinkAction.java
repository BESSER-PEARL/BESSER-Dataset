





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_LinkAction extends Action {






    private List<UML2WithID_LinkEndData> uml2withid_linkenddatas;


    public UML2WithID_LinkAction(
    ) {
        super(
        );
        this.uml2withid_linkenddatas = new ArrayList<>();
    }

    public UML2WithID_LinkAction(
        ArrayList<UML2WithID_LinkEndData> uml2withid_linkenddatas    ) {
        this.uml2withid_linkenddatas = uml2withid_linkenddatas;
    }


    public List<UML2WithID_LinkEndData> getUml2withid_linkenddatas() {
        return uml2withid_linkenddatas;
    }

    public void addUml2withid_linkenddata(Uml2withid_linkenddata uml2withid_linkenddata) {
        this.uml2withid_linkenddatas.add(uml2withid_linkenddata);
    }

}