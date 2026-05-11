





import java.util.List;
import java.util.ArrayList;

public class xal_Premise  {

    private String premiseThoroughfareConnector;
    private String premiseDependencyType;
    private String premiseDependency;
    private String type;
    private String anyAttribute;
    private String any;





    private List<xal_AddressLine> xal_addresslines;




    private List<xal_PremiseName> xal_premisenames;




    private xal_MailStop xal_mailstop;




    private xal_Thoroughfare xal_thoroughfare;




    private xal_Premise xal_premise;




    private xal_PremiseNumberRange xal_premisenumberrange;




    private xal_DependentLocality xal_dependentlocality;




    private xal_PremiseLocation xal_premiselocation;




    private xal_PostalCode xal_postalcode;




    private List<xal_SubPremise> xal_subpremises;




    private xal_Locality xal_locality;




    private List<xal_BuildingName> xal_buildingnames;


    public xal_Premise(
        String premiseThoroughfareConnector,        String premiseDependencyType,        String premiseDependency,        String type,        String anyAttribute,        String any    ) {
        this.premiseThoroughfareConnector = premiseThoroughfareConnector;
        this.premiseDependencyType = premiseDependencyType;
        this.premiseDependency = premiseDependency;
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.any = any;
        this.xal_addresslines = new ArrayList<>();
        this.xal_premisenames = new ArrayList<>();
        this.xal_subpremises = new ArrayList<>();
        this.xal_buildingnames = new ArrayList<>();
    }

    public xal_Premise(
        String premiseThoroughfareConnector,        String premiseDependencyType,        String premiseDependency,        String type,        String anyAttribute,        String any        ArrayList<xal_AddressLine> xal_addresslines,        ArrayList<xal_PremiseName> xal_premisenames,        ArrayList<xal_SubPremise> xal_subpremises,        ArrayList<xal_BuildingName> xal_buildingnames    ) {
        this.premiseThoroughfareConnector = premiseThoroughfareConnector;
        this.premiseDependencyType = premiseDependencyType;
        this.premiseDependency = premiseDependency;
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.any = any;
        this.xal_addresslines = xal_addresslines;
        this.xal_premisenames = xal_premisenames;
        this.xal_subpremises = xal_subpremises;
        this.xal_buildingnames = xal_buildingnames;
    }

    public String getPremisethoroughfareconnector() {
        return premiseThoroughfareConnector;
    }

    public void setPremisethoroughfareconnector(String premiseThoroughfareConnector) {
        this.premiseThoroughfareConnector = premiseThoroughfareConnector;
    }
    public String getPremisedependencytype() {
        return premiseDependencyType;
    }

    public void setPremisedependencytype(String premiseDependencyType) {
        this.premiseDependencyType = premiseDependencyType;
    }
    public String getPremisedependency() {
        return premiseDependency;
    }

    public void setPremisedependency(String premiseDependency) {
        this.premiseDependency = premiseDependency;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }

    public List<xal_AddressLine> getXal_addresslines() {
        return xal_addresslines;
    }

    public void addXal_addressline(Xal_addressline xal_addressline) {
        this.xal_addresslines.add(xal_addressline);
    }
    public List<xal_PremiseName> getXal_premisenames() {
        return xal_premisenames;
    }

    public void addXal_premisename(Xal_premisename xal_premisename) {
        this.xal_premisenames.add(xal_premisename);
    }
    public xal_MailStop getXal_mailstop() {
        return xal_mailstop;
    }

    public void setXal_mailstop(xal_MailStop xal_mailstop) {
        this.xal_mailstop = xal_mailstop;
    }
    public xal_Thoroughfare getXal_thoroughfare() {
        return xal_thoroughfare;
    }

    public void setXal_thoroughfare(xal_Thoroughfare xal_thoroughfare) {
        this.xal_thoroughfare = xal_thoroughfare;
    }
    public xal_Premise getXal_premise() {
        return xal_premise;
    }

    public void setXal_premise(xal_Premise xal_premise) {
        this.xal_premise = xal_premise;
    }
    public xal_PremiseNumberRange getXal_premisenumberrange() {
        return xal_premisenumberrange;
    }

    public void setXal_premisenumberrange(xal_PremiseNumberRange xal_premisenumberrange) {
        this.xal_premisenumberrange = xal_premisenumberrange;
    }
    public xal_DependentLocality getXal_dependentlocality() {
        return xal_dependentlocality;
    }

    public void setXal_dependentlocality(xal_DependentLocality xal_dependentlocality) {
        this.xal_dependentlocality = xal_dependentlocality;
    }
    public xal_PremiseLocation getXal_premiselocation() {
        return xal_premiselocation;
    }

    public void setXal_premiselocation(xal_PremiseLocation xal_premiselocation) {
        this.xal_premiselocation = xal_premiselocation;
    }
    public xal_PostalCode getXal_postalcode() {
        return xal_postalcode;
    }

    public void setXal_postalcode(xal_PostalCode xal_postalcode) {
        this.xal_postalcode = xal_postalcode;
    }
    public List<xal_SubPremise> getXal_subpremises() {
        return xal_subpremises;
    }

    public void addXal_subpremise(Xal_subpremise xal_subpremise) {
        this.xal_subpremises.add(xal_subpremise);
    }
    public xal_Locality getXal_locality() {
        return xal_locality;
    }

    public void setXal_locality(xal_Locality xal_locality) {
        this.xal_locality = xal_locality;
    }
    public List<xal_BuildingName> getXal_buildingnames() {
        return xal_buildingnames;
    }

    public void addXal_buildingname(Xal_buildingname xal_buildingname) {
        this.xal_buildingnames.add(xal_buildingname);
    }

}