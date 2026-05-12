





import java.util.List;
import java.util.ArrayList;

public class XHTML_Blockquote extends Attrs, Blocktext {






    private List<Block> blocks;




    private URI uri;


    public XHTML_Blockquote(
    ) {
        super(
        );
        this.blocks = new ArrayList<>();
    }

    public XHTML_Blockquote(
        ArrayList<Block> blocks    ) {
        this.blocks = blocks;
    }


    public List<Block> getBlocks() {
        return blocks;
    }

    public void addBlock(Block block) {
        this.blocks.add(block);
    }
    public URI getUri() {
        return uri;
    }

    public void setUri(URI uri) {
        this.uri = uri;
    }

}