





import java.util.List;
import java.util.ArrayList;

public class VHDLModel_CompositeBlock extends ComplexBlock {






    private VHDLModel_BlockRef vhdlmodel_blockref;




    private List<VHDLModel_Block> vhdlmodel_blocks;


    public VHDLModel_CompositeBlock(
    ) {
        super(
        );
        this.vhdlmodel_blocks = new ArrayList<>();
    }

    public VHDLModel_CompositeBlock(
        ArrayList<VHDLModel_Block> vhdlmodel_blocks    ) {
        this.vhdlmodel_blocks = vhdlmodel_blocks;
    }


    public VHDLModel_BlockRef getVhdlmodel_blockref() {
        return vhdlmodel_blockref;
    }

    public void setVhdlmodel_blockref(VHDLModel_BlockRef vhdlmodel_blockref) {
        this.vhdlmodel_blockref = vhdlmodel_blockref;
    }
    public List<VHDLModel_Block> getVhdlmodel_blocks() {
        return vhdlmodel_blocks;
    }

    public void addVhdlmodel_block(Vhdlmodel_block vhdlmodel_block) {
        this.vhdlmodel_blocks.add(vhdlmodel_block);
    }

}