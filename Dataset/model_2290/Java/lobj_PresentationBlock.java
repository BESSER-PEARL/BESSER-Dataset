





import java.util.List;
import java.util.ArrayList;

public class lobj_PresentationBlock  {

    private int lod;
    private String rendering;
    private String id;





    private lobj_Block lobj_block;




    private lobj_CorrBlock lobj_corrblock;


    public lobj_PresentationBlock(
        int lod,        String rendering,        String id    ) {
        this.lod = lod;
        this.rendering = rendering;
        this.id = id;
    }


    public int getLod() {
        return lod;
    }

    public void setLod(int lod) {
        this.lod = lod;
    }
    public String getRendering() {
        return rendering;
    }

    public void setRendering(String rendering) {
        this.rendering = rendering;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public lobj_Block getLobj_block() {
        return lobj_block;
    }

    public void setLobj_block(lobj_Block lobj_block) {
        this.lobj_block = lobj_block;
    }
    public lobj_CorrBlock getLobj_corrblock() {
        return lobj_corrblock;
    }

    public void setLobj_corrblock(lobj_CorrBlock lobj_corrblock) {
        this.lobj_corrblock = lobj_corrblock;
    }

}