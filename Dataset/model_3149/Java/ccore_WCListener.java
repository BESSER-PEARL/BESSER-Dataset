





import java.util.List;
import java.util.ArrayList;

public class ccore_WCListener  {






    private List<ccore_ItemType> ccore_itemtypes;




    private ccore_Attribute ccore_attribute;




    private List<ccore_Attribute> ccore_attributes;




    private ccore_ItemType ccore_itemtype;


    public ccore_WCListener(
    ) {
        this.ccore_itemtypes = new ArrayList<>();
        this.ccore_attributes = new ArrayList<>();
    }

    public ccore_WCListener(
        ArrayList<ccore_ItemType> ccore_itemtypes,        ArrayList<ccore_Attribute> ccore_attributes    ) {
        this.ccore_itemtypes = ccore_itemtypes;
        this.ccore_attributes = ccore_attributes;
    }


    public List<ccore_ItemType> getCcore_itemtypes() {
        return ccore_itemtypes;
    }

    public void addCcore_itemtype(Ccore_itemtype ccore_itemtype) {
        this.ccore_itemtypes.add(ccore_itemtype);
    }
    public ccore_Attribute getCcore_attribute() {
        return ccore_attribute;
    }

    public void setCcore_attribute(ccore_Attribute ccore_attribute) {
        this.ccore_attribute = ccore_attribute;
    }
    public List<ccore_Attribute> getCcore_attributes() {
        return ccore_attributes;
    }

    public void addCcore_attribute(Ccore_attribute ccore_attribute) {
        this.ccore_attributes.add(ccore_attribute);
    }
    public ccore_ItemType getCcore_itemtype() {
        return ccore_itemtype;
    }

    public void setCcore_itemtype(ccore_ItemType ccore_itemtype) {
        this.ccore_itemtype = ccore_itemtype;
    }

}