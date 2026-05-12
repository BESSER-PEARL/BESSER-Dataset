





import java.util.List;
import java.util.ArrayList;

public class org_k1s_nppn_Container extends Block {






    private List<nppn_Block> nppn_blocks;


    public org_k1s_nppn_Container(
    ) {
        super(
        );
        this.nppn_blocks = new ArrayList<>();
    }

    public org_k1s_nppn_Container(
        ArrayList<nppn_Block> nppn_blocks    ) {
        this.nppn_blocks = nppn_blocks;
    }


    public List<nppn_Block> getNppn_blocks() {
        return nppn_blocks;
    }

    public void addNppn_block(Nppn_block nppn_block) {
        this.nppn_blocks.add(nppn_block);
    }

}