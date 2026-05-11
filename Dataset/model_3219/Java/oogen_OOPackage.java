





import java.util.List;
import java.util.ArrayList;

public class oogen_OOPackage  {

    private String name;





    private List<oogen_OOClass> oogen_ooclasss;




    private oogen_OOClass oogen_ooclass;




    private oogen_OOEnumeration oogen_ooenumeration;




    private List<oogen_OOEnumeration> oogen_ooenumerations;


    public oogen_OOPackage(
        String name    ) {
        this.name = name;
        this.oogen_ooclasss = new ArrayList<>();
        this.oogen_ooenumerations = new ArrayList<>();
    }

    public oogen_OOPackage(
        String name        ArrayList<oogen_OOClass> oogen_ooclasss,        ArrayList<oogen_OOEnumeration> oogen_ooenumerations    ) {
        this.name = name;
        this.oogen_ooclasss = oogen_ooclasss;
        this.oogen_ooenumerations = oogen_ooenumerations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<oogen_OOClass> getOogen_ooclasss() {
        return oogen_ooclasss;
    }

    public void addOogen_ooclass(Oogen_ooclass oogen_ooclass) {
        this.oogen_ooclasss.add(oogen_ooclass);
    }
    public oogen_OOClass getOogen_ooclass() {
        return oogen_ooclass;
    }

    public void setOogen_ooclass(oogen_OOClass oogen_ooclass) {
        this.oogen_ooclass = oogen_ooclass;
    }
    public oogen_OOEnumeration getOogen_ooenumeration() {
        return oogen_ooenumeration;
    }

    public void setOogen_ooenumeration(oogen_OOEnumeration oogen_ooenumeration) {
        this.oogen_ooenumeration = oogen_ooenumeration;
    }
    public List<oogen_OOEnumeration> getOogen_ooenumerations() {
        return oogen_ooenumerations;
    }

    public void addOogen_ooenumeration(Oogen_ooenumeration oogen_ooenumeration) {
        this.oogen_ooenumerations.add(oogen_ooenumeration);
    }

}