





import java.util.List;
import java.util.ArrayList;

public class ccore_Item extends DBObject, ENamedElement {

    private boolean isvalid;
    private boolean twRequireNewRev;
    private String displayName;
    private String twCommittedDate;
    private int twVersion;
    private boolean twRevModified;
    private String qualifiedName;
    private boolean itemHidden;
    private boolean itemReadonly;
    private String committedBy;





    private ccore_BindingDesc ccore_bindingdesc;




    private List<ccore_Attribute> ccore_attributes;




    private ccore_Cadse ccore_cadse;




    private ccore_BindingDesc ccore_bindingdesc;




    private ccore_Item ccore_item;




    private ccore_Cadse ccore_cadse;




    private List<ccore_ItemType> ccore_itemtypes;


    public ccore_Item(
        boolean isvalid,        boolean twRequireNewRev,        String displayName,        String twCommittedDate,        int twVersion,        boolean twRevModified,        String qualifiedName,        boolean itemHidden,        boolean itemReadonly,        String committedBy    ) {
        super(
        );
        this.isvalid = isvalid;
        this.twRequireNewRev = twRequireNewRev;
        this.displayName = displayName;
        this.twCommittedDate = twCommittedDate;
        this.twVersion = twVersion;
        this.twRevModified = twRevModified;
        this.qualifiedName = qualifiedName;
        this.itemHidden = itemHidden;
        this.itemReadonly = itemReadonly;
        this.committedBy = committedBy;
        this.ccore_attributes = new ArrayList<>();
        this.ccore_itemtypes = new ArrayList<>();
    }

    public ccore_Item(
        boolean isvalid,        boolean twRequireNewRev,        String displayName,        String twCommittedDate,        int twVersion,        boolean twRevModified,        String qualifiedName,        boolean itemHidden,        boolean itemReadonly,        String committedBy        ArrayList<ccore_Attribute> ccore_attributes,        ArrayList<ccore_ItemType> ccore_itemtypes    ) {
        this.isvalid = isvalid;
        this.twRequireNewRev = twRequireNewRev;
        this.displayName = displayName;
        this.twCommittedDate = twCommittedDate;
        this.twVersion = twVersion;
        this.twRevModified = twRevModified;
        this.qualifiedName = qualifiedName;
        this.itemHidden = itemHidden;
        this.itemReadonly = itemReadonly;
        this.committedBy = committedBy;
        this.ccore_attributes = ccore_attributes;
        this.ccore_itemtypes = ccore_itemtypes;
    }

    public boolean getIsvalid() {
        return isvalid;
    }

    public void setIsvalid(boolean isvalid) {
        this.isvalid = isvalid;
    }
    public boolean getTwrequirenewrev() {
        return twRequireNewRev;
    }

    public void setTwrequirenewrev(boolean twRequireNewRev) {
        this.twRequireNewRev = twRequireNewRev;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }
    public String getTwcommitteddate() {
        return twCommittedDate;
    }

    public void setTwcommitteddate(String twCommittedDate) {
        this.twCommittedDate = twCommittedDate;
    }
    public int getTwversion() {
        return twVersion;
    }

    public void setTwversion(int twVersion) {
        this.twVersion = twVersion;
    }
    public boolean getTwrevmodified() {
        return twRevModified;
    }

    public void setTwrevmodified(boolean twRevModified) {
        this.twRevModified = twRevModified;
    }
    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }
    public boolean getItemhidden() {
        return itemHidden;
    }

    public void setItemhidden(boolean itemHidden) {
        this.itemHidden = itemHidden;
    }
    public boolean getItemreadonly() {
        return itemReadonly;
    }

    public void setItemreadonly(boolean itemReadonly) {
        this.itemReadonly = itemReadonly;
    }
    public String getCommittedby() {
        return committedBy;
    }

    public void setCommittedby(String committedBy) {
        this.committedBy = committedBy;
    }

    public ccore_BindingDesc getCcore_bindingdesc() {
        return ccore_bindingdesc;
    }

    public void setCcore_bindingdesc(ccore_BindingDesc ccore_bindingdesc) {
        this.ccore_bindingdesc = ccore_bindingdesc;
    }
    public List<ccore_Attribute> getCcore_attributes() {
        return ccore_attributes;
    }

    public void addCcore_attribute(Ccore_attribute ccore_attribute) {
        this.ccore_attributes.add(ccore_attribute);
    }
    public ccore_Cadse getCcore_cadse() {
        return ccore_cadse;
    }

    public void setCcore_cadse(ccore_Cadse ccore_cadse) {
        this.ccore_cadse = ccore_cadse;
    }
    public ccore_BindingDesc getCcore_bindingdesc() {
        return ccore_bindingdesc;
    }

    public void setCcore_bindingdesc(ccore_BindingDesc ccore_bindingdesc) {
        this.ccore_bindingdesc = ccore_bindingdesc;
    }
    public ccore_Item getCcore_item() {
        return ccore_item;
    }

    public void setCcore_item(ccore_Item ccore_item) {
        this.ccore_item = ccore_item;
    }
    public ccore_Cadse getCcore_cadse() {
        return ccore_cadse;
    }

    public void setCcore_cadse(ccore_Cadse ccore_cadse) {
        this.ccore_cadse = ccore_cadse;
    }
    public List<ccore_ItemType> getCcore_itemtypes() {
        return ccore_itemtypes;
    }

    public void addCcore_itemtype(Ccore_itemtype ccore_itemtype) {
        this.ccore_itemtypes.add(ccore_itemtype);
    }

}