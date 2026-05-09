





import java.util.List;
import java.util.ArrayList;

public class presentation_CoolBar extends Composite {

    private String locked;
    private String itemSizes;
    private String itemOrder;
    private String group3;
    private String wrapIndices;



    public presentation_CoolBar(
        String locked,        String itemSizes,        String itemOrder,        String group3,        String wrapIndices    ) {
        super(
        );
        this.locked = locked;
        this.itemSizes = itemSizes;
        this.itemOrder = itemOrder;
        this.group3 = group3;
        this.wrapIndices = wrapIndices;
    }


    public String getLocked() {
        return locked;
    }

    public void setLocked(String locked) {
        this.locked = locked;
    }
    public String getItemsizes() {
        return itemSizes;
    }

    public void setItemsizes(String itemSizes) {
        this.itemSizes = itemSizes;
    }
    public String getItemorder() {
        return itemOrder;
    }

    public void setItemorder(String itemOrder) {
        this.itemOrder = itemOrder;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getWrapindices() {
        return wrapIndices;
    }

    public void setWrapindices(String wrapIndices) {
        this.wrapIndices = wrapIndices;
    }


}