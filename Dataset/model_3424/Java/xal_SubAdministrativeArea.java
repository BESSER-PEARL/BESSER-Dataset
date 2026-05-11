





import java.util.List;
import java.util.ArrayList;

public class xal_SubAdministrativeArea  {

    private String anyAttribute;
    private String indicator;
    private String any;
    private String usageType;
    private String type;





    private List<xal_SubAdministrativeAreaName> xal_subadministrativeareanames;




    private xal_Locality xal_locality;




    private xal_AdministrativeArea xal_administrativearea;




    private List<xal_AddressLine> xal_addresslines;


    public xal_SubAdministrativeArea(
        String anyAttribute,        String indicator,        String any,        String usageType,        String type    ) {
        this.anyAttribute = anyAttribute;
        this.indicator = indicator;
        this.any = any;
        this.usageType = usageType;
        this.type = type;
        this.xal_subadministrativeareanames = new ArrayList<>();
        this.xal_addresslines = new ArrayList<>();
    }

    public xal_SubAdministrativeArea(
        String anyAttribute,        String indicator,        String any,        String usageType,        String type        ArrayList<xal_SubAdministrativeAreaName> xal_subadministrativeareanames,        ArrayList<xal_AddressLine> xal_addresslines    ) {
        this.anyAttribute = anyAttribute;
        this.indicator = indicator;
        this.any = any;
        this.usageType = usageType;
        this.type = type;
        this.xal_subadministrativeareanames = xal_subadministrativeareanames;
        this.xal_addresslines = xal_addresslines;
    }

    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getIndicator() {
        return indicator;
    }

    public void setIndicator(String indicator) {
        this.indicator = indicator;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getUsagetype() {
        return usageType;
    }

    public void setUsagetype(String usageType) {
        this.usageType = usageType;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<xal_SubAdministrativeAreaName> getXal_subadministrativeareanames() {
        return xal_subadministrativeareanames;
    }

    public void addXal_subadministrativeareaname(Xal_subadministrativeareaname xal_subadministrativeareaname) {
        this.xal_subadministrativeareanames.add(xal_subadministrativeareaname);
    }
    public xal_Locality getXal_locality() {
        return xal_locality;
    }

    public void setXal_locality(xal_Locality xal_locality) {
        this.xal_locality = xal_locality;
    }
    public xal_AdministrativeArea getXal_administrativearea() {
        return xal_administrativearea;
    }

    public void setXal_administrativearea(xal_AdministrativeArea xal_administrativearea) {
        this.xal_administrativearea = xal_administrativearea;
    }
    public List<xal_AddressLine> getXal_addresslines() {
        return xal_addresslines;
    }

    public void addXal_addressline(Xal_addressline xal_addressline) {
        this.xal_addresslines.add(xal_addressline);
    }

}