





import java.util.List;
import java.util.ArrayList;

public class express_core_EnumerationType extends DefinedType {

    private String isExtensible;





    private EnumerationType enumerationtype;




    private List<EnumerationType> enumerationtypes;




    private List<EnumerationItem> enumerationitems;




    private List<EnumerationItem> enumerationitems;


    public express_core_EnumerationType(
        String isExtensible    ) {
        super(
        );
        this.isExtensible = isExtensible;
        this.enumerationtypes = new ArrayList<>();
        this.enumerationitems = new ArrayList<>();
        this.enumerationitems = new ArrayList<>();
    }

    public express_core_EnumerationType(
        String isExtensible        ArrayList<EnumerationType> enumerationtypes,        ArrayList<EnumerationItem> enumerationitems,        ArrayList<EnumerationItem> enumerationitems    ) {
        this.isExtensible = isExtensible;
        this.enumerationtypes = enumerationtypes;
        this.enumerationitems = enumerationitems;
        this.enumerationitems = enumerationitems;
    }

    public String getIsextensible() {
        return isExtensible;
    }

    public void setIsextensible(String isExtensible) {
        this.isExtensible = isExtensible;
    }

    public EnumerationType getEnumerationtype() {
        return enumerationtype;
    }

    public void setEnumerationtype(EnumerationType enumerationtype) {
        this.enumerationtype = enumerationtype;
    }
    public List<EnumerationType> getEnumerationtypes() {
        return enumerationtypes;
    }

    public void addEnumerationtype(Enumerationtype enumerationtype) {
        this.enumerationtypes.add(enumerationtype);
    }
    public List<EnumerationItem> getEnumerationitems() {
        return enumerationitems;
    }

    public void addEnumerationitem(Enumerationitem enumerationitem) {
        this.enumerationitems.add(enumerationitem);
    }
    public List<EnumerationItem> getEnumerationitems() {
        return enumerationitems;
    }

    public void addEnumerationitem(Enumerationitem enumerationitem) {
        this.enumerationitems.add(enumerationitem);
    }

}