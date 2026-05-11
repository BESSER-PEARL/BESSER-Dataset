





import java.util.List;
import java.util.ArrayList;

public class VHDLModel_Block  {

    private String name;





    private List<VHDLModel_InputPort> vhdlmodel_inputports;


    public VHDLModel_Block(
        String name    ) {
        this.name = name;
        this.vhdlmodel_inputports = new ArrayList<>();
    }

    public VHDLModel_Block(
        String name        ArrayList<VHDLModel_InputPort> vhdlmodel_inputports    ) {
        this.name = name;
        this.vhdlmodel_inputports = vhdlmodel_inputports;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<VHDLModel_InputPort> getVhdlmodel_inputports() {
        return vhdlmodel_inputports;
    }

    public void addVhdlmodel_inputport(Vhdlmodel_inputport vhdlmodel_inputport) {
        this.vhdlmodel_inputports.add(vhdlmodel_inputport);
    }

}