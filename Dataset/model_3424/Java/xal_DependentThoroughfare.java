





import java.util.List;
import java.util.ArrayList;

public class xal_DependentThoroughfare  {

    private String anyAttribute;
    private String type;
    private String any;





    private xal_ThoroughfareTrailingType xal_thoroughfaretrailingtype;




    private List<xal_AddressLine> xal_addresslines;




    private xal_ThoroughfarePostDirection xal_thoroughfarepostdirection;




    private List<xal_ThoroughfareName> xal_thoroughfarenames;




    private xal_ThoroughfareLeadingType xal_thoroughfareleadingtype;




    private xal_Thoroughfare xal_thoroughfare;


    public xal_DependentThoroughfare(
        String anyAttribute,        String type,        String any    ) {
        this.anyAttribute = anyAttribute;
        this.type = type;
        this.any = any;
        this.xal_addresslines = new ArrayList<>();
        this.xal_thoroughfarenames = new ArrayList<>();
    }

    public xal_DependentThoroughfare(
        String anyAttribute,        String type,        String any        ArrayList<xal_AddressLine> xal_addresslines,        ArrayList<xal_ThoroughfareName> xal_thoroughfarenames    ) {
        this.anyAttribute = anyAttribute;
        this.type = type;
        this.any = any;
        this.xal_addresslines = xal_addresslines;
        this.xal_thoroughfarenames = xal_thoroughfarenames;
    }

    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }

    public xal_ThoroughfareTrailingType getXal_thoroughfaretrailingtype() {
        return xal_thoroughfaretrailingtype;
    }

    public void setXal_thoroughfaretrailingtype(xal_ThoroughfareTrailingType xal_thoroughfaretrailingtype) {
        this.xal_thoroughfaretrailingtype = xal_thoroughfaretrailingtype;
    }
    public List<xal_AddressLine> getXal_addresslines() {
        return xal_addresslines;
    }

    public void addXal_addressline(Xal_addressline xal_addressline) {
        this.xal_addresslines.add(xal_addressline);
    }
    public xal_ThoroughfarePostDirection getXal_thoroughfarepostdirection() {
        return xal_thoroughfarepostdirection;
    }

    public void setXal_thoroughfarepostdirection(xal_ThoroughfarePostDirection xal_thoroughfarepostdirection) {
        this.xal_thoroughfarepostdirection = xal_thoroughfarepostdirection;
    }
    public List<xal_ThoroughfareName> getXal_thoroughfarenames() {
        return xal_thoroughfarenames;
    }

    public void addXal_thoroughfarename(Xal_thoroughfarename xal_thoroughfarename) {
        this.xal_thoroughfarenames.add(xal_thoroughfarename);
    }
    public xal_ThoroughfareLeadingType getXal_thoroughfareleadingtype() {
        return xal_thoroughfareleadingtype;
    }

    public void setXal_thoroughfareleadingtype(xal_ThoroughfareLeadingType xal_thoroughfareleadingtype) {
        this.xal_thoroughfareleadingtype = xal_thoroughfareleadingtype;
    }
    public xal_Thoroughfare getXal_thoroughfare() {
        return xal_thoroughfare;
    }

    public void setXal_thoroughfare(xal_Thoroughfare xal_thoroughfare) {
        this.xal_thoroughfare = xal_thoroughfare;
    }

}