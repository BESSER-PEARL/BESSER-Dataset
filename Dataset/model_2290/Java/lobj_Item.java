





import java.util.List;
import java.util.ArrayList;

public class lobj_Item  {

    private String luRef;
    private String id;





    private List<lobj_Item> lobj_items;




    private List<lobj_CorrBlock> lobj_corrblocks;




    private lobj_LearningUnit lobj_learningunit;


    public lobj_Item(
        String luRef,        String id    ) {
        this.luRef = luRef;
        this.id = id;
        this.lobj_items = new ArrayList<>();
        this.lobj_corrblocks = new ArrayList<>();
    }

    public lobj_Item(
        String luRef,        String id        ArrayList<lobj_Item> lobj_items,        ArrayList<lobj_CorrBlock> lobj_corrblocks    ) {
        this.luRef = luRef;
        this.id = id;
        this.lobj_items = lobj_items;
        this.lobj_corrblocks = lobj_corrblocks;
    }

    public String getLuref() {
        return luRef;
    }

    public void setLuref(String luRef) {
        this.luRef = luRef;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<lobj_Item> getLobj_items() {
        return lobj_items;
    }

    public void addLobj_item(Lobj_item lobj_item) {
        this.lobj_items.add(lobj_item);
    }
    public List<lobj_CorrBlock> getLobj_corrblocks() {
        return lobj_corrblocks;
    }

    public void addLobj_corrblock(Lobj_corrblock lobj_corrblock) {
        this.lobj_corrblocks.add(lobj_corrblock);
    }
    public lobj_LearningUnit getLobj_learningunit() {
        return lobj_learningunit;
    }

    public void setLobj_learningunit(lobj_LearningUnit lobj_learningunit) {
        this.lobj_learningunit = lobj_learningunit;
    }

}