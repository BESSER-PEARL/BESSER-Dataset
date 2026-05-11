





import java.util.List;
import java.util.ArrayList;

public class lobj_BlockFolder extends LearningObject {






    private lobj_FolderMeta lobj_foldermeta;




    private lobj_BlockFolder lobj_blockfolder;




    private List<lobj_Block> lobj_blocks;


    public lobj_BlockFolder(
    ) {
        super(
        );
        this.lobj_blocks = new ArrayList<>();
    }

    public lobj_BlockFolder(
        ArrayList<lobj_Block> lobj_blocks    ) {
        this.lobj_blocks = lobj_blocks;
    }


    public lobj_FolderMeta getLobj_foldermeta() {
        return lobj_foldermeta;
    }

    public void setLobj_foldermeta(lobj_FolderMeta lobj_foldermeta) {
        this.lobj_foldermeta = lobj_foldermeta;
    }
    public lobj_BlockFolder getLobj_blockfolder() {
        return lobj_blockfolder;
    }

    public void setLobj_blockfolder(lobj_BlockFolder lobj_blockfolder) {
        this.lobj_blockfolder = lobj_blockfolder;
    }
    public List<lobj_Block> getLobj_blocks() {
        return lobj_blocks;
    }

    public void addLobj_block(Lobj_block lobj_block) {
        this.lobj_blocks.add(lobj_block);
    }

}