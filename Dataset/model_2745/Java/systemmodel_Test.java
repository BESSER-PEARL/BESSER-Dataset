





import java.util.List;
import java.util.ArrayList;

public class systemmodel_Test extends Block {






    private List<systemmodel_Block> systemmodel_blocks;


    public systemmodel_Test(
    ) {
        super(
        );
        this.systemmodel_blocks = new ArrayList<>();
    }

    public systemmodel_Test(
        ArrayList<systemmodel_Block> systemmodel_blocks    ) {
        this.systemmodel_blocks = systemmodel_blocks;
    }


    public List<systemmodel_Block> getSystemmodel_blocks() {
        return systemmodel_blocks;
    }

    public void addSystemmodel_block(Systemmodel_block systemmodel_block) {
        this.systemmodel_blocks.add(systemmodel_block);
    }

}