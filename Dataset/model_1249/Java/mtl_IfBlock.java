





import java.util.List;
import java.util.ArrayList;

public class mtl_IfBlock extends Block {






    private mtl_Block mtl_block;




    private List<mtl_IfBlock> mtl_ifblocks;


    public mtl_IfBlock(
    ) {
        super(
        );
        this.mtl_ifblocks = new ArrayList<>();
    }

    public mtl_IfBlock(
        ArrayList<mtl_IfBlock> mtl_ifblocks    ) {
        this.mtl_ifblocks = mtl_ifblocks;
    }


    public mtl_Block getMtl_block() {
        return mtl_block;
    }

    public void setMtl_block(mtl_Block mtl_block) {
        this.mtl_block = mtl_block;
    }
    public List<mtl_IfBlock> getMtl_ifblocks() {
        return mtl_ifblocks;
    }

    public void addMtl_ifblock(Mtl_ifblock mtl_ifblock) {
        this.mtl_ifblocks.add(mtl_ifblock);
    }

}