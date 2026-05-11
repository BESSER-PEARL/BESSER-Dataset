





import java.util.List;
import java.util.ArrayList;

public class ccore_DBObject  {

    private String uuid_lsb;
    private String uuid_msb;
    private int objectId;





    private ccore_ItemType ccore_itemtype;


    public ccore_DBObject(
        String uuid_lsb,        String uuid_msb,        int objectId    ) {
        this.uuid_lsb = uuid_lsb;
        this.uuid_msb = uuid_msb;
        this.objectId = objectId;
    }


    public String getUuid_lsb() {
        return uuid_lsb;
    }

    public void setUuid_lsb(String uuid_lsb) {
        this.uuid_lsb = uuid_lsb;
    }
    public String getUuid_msb() {
        return uuid_msb;
    }

    public void setUuid_msb(String uuid_msb) {
        this.uuid_msb = uuid_msb;
    }
    public int getObjectid() {
        return objectId;
    }

    public void setObjectid(int objectId) {
        this.objectId = objectId;
    }

    public ccore_ItemType getCcore_itemtype() {
        return ccore_itemtype;
    }

    public void setCcore_itemtype(ccore_ItemType ccore_itemtype) {
        this.ccore_itemtype = ccore_itemtype;
    }

}