





import java.util.List;
import java.util.ArrayList;

public class adb_PackageSpecification  {

    private String endname;





    private List<adb_BasicDeclarativeItem> adb_basicdeclarativeitems;




    private List<adb_BasicDeclarativeItem> adb_basicdeclarativeitems;




    private adb_PackageDefinition adb_packagedefinition;


    public adb_PackageSpecification(
        String endname    ) {
        this.endname = endname;
        this.adb_basicdeclarativeitems = new ArrayList<>();
        this.adb_basicdeclarativeitems = new ArrayList<>();
    }

    public adb_PackageSpecification(
        String endname        ArrayList<adb_BasicDeclarativeItem> adb_basicdeclarativeitems,        ArrayList<adb_BasicDeclarativeItem> adb_basicdeclarativeitems    ) {
        this.endname = endname;
        this.adb_basicdeclarativeitems = adb_basicdeclarativeitems;
        this.adb_basicdeclarativeitems = adb_basicdeclarativeitems;
    }

    public String getEndname() {
        return endname;
    }

    public void setEndname(String endname) {
        this.endname = endname;
    }

    public List<adb_BasicDeclarativeItem> getAdb_basicdeclarativeitems() {
        return adb_basicdeclarativeitems;
    }

    public void addAdb_basicdeclarativeitem(Adb_basicdeclarativeitem adb_basicdeclarativeitem) {
        this.adb_basicdeclarativeitems.add(adb_basicdeclarativeitem);
    }
    public List<adb_BasicDeclarativeItem> getAdb_basicdeclarativeitems() {
        return adb_basicdeclarativeitems;
    }

    public void addAdb_basicdeclarativeitem(Adb_basicdeclarativeitem adb_basicdeclarativeitem) {
        this.adb_basicdeclarativeitems.add(adb_basicdeclarativeitem);
    }
    public adb_PackageDefinition getAdb_packagedefinition() {
        return adb_packagedefinition;
    }

    public void setAdb_packagedefinition(adb_PackageDefinition adb_packagedefinition) {
        this.adb_packagedefinition = adb_packagedefinition;
    }

}