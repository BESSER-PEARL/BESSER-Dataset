





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Association extends NamedElement {

    private String isDerived;





    private List<uml2CD_Property> uml2cd_propertys;




    private uml2CD_Package uml2cd_package;




    private List<uml2CD_Property> uml2cd_propertys;


    public uml2CD_Association(
        String isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
        this.uml2cd_propertys = new ArrayList<>();
        this.uml2cd_propertys = new ArrayList<>();
    }

    public uml2CD_Association(
        String isDerived        ArrayList<uml2CD_Property> uml2cd_propertys,        ArrayList<uml2CD_Property> uml2cd_propertys    ) {
        this.isDerived = isDerived;
        this.uml2cd_propertys = uml2cd_propertys;
        this.uml2cd_propertys = uml2cd_propertys;
    }

    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }

    public List<uml2CD_Property> getUml2cd_propertys() {
        return uml2cd_propertys;
    }

    public void addUml2cd_property(Uml2cd_property uml2cd_property) {
        this.uml2cd_propertys.add(uml2cd_property);
    }
    public uml2CD_Package getUml2cd_package() {
        return uml2cd_package;
    }

    public void setUml2cd_package(uml2CD_Package uml2cd_package) {
        this.uml2cd_package = uml2cd_package;
    }
    public List<uml2CD_Property> getUml2cd_propertys() {
        return uml2cd_propertys;
    }

    public void addUml2cd_property(Uml2cd_property uml2cd_property) {
        this.uml2cd_propertys.add(uml2cd_property);
    }

}