





import java.util.List;
import java.util.ArrayList;

public class VHDLModel_VHDLSpecification  {

    private String name;





    private List<VHDLModel_CompositeBlock> vhdlmodel_compositeblocks;


    public VHDLModel_VHDLSpecification(
        String name    ) {
        this.name = name;
        this.vhdlmodel_compositeblocks = new ArrayList<>();
    }

    public VHDLModel_VHDLSpecification(
        String name        ArrayList<VHDLModel_CompositeBlock> vhdlmodel_compositeblocks    ) {
        this.name = name;
        this.vhdlmodel_compositeblocks = vhdlmodel_compositeblocks;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<VHDLModel_CompositeBlock> getVhdlmodel_compositeblocks() {
        return vhdlmodel_compositeblocks;
    }

    public void addVhdlmodel_compositeblock(Vhdlmodel_compositeblock vhdlmodel_compositeblock) {
        this.vhdlmodel_compositeblocks.add(vhdlmodel_compositeblock);
    }

}