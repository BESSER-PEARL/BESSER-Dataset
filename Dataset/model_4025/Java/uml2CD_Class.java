





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Class extends NamedElement {

    private String active;





    private List<uml2CD_Property> uml2cd_propertys;




    private uml2CD_Package uml2cd_package;




    private List<uml2CD_Operation> uml2cd_operations;


    public uml2CD_Class(
        String active    ) {
        super(
        );
        this.active = active;
        this.uml2cd_propertys = new ArrayList<>();
        this.uml2cd_operations = new ArrayList<>();
    }

    public uml2CD_Class(
        String active        ArrayList<uml2CD_Property> uml2cd_propertys,        ArrayList<uml2CD_Operation> uml2cd_operations    ) {
        this.active = active;
        this.uml2cd_propertys = uml2cd_propertys;
        this.uml2cd_operations = uml2cd_operations;
    }

    public String getActive() {
        return active;
    }

    public void setActive(String active) {
        this.active = active;
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
    public List<uml2CD_Operation> getUml2cd_operations() {
        return uml2cd_operations;
    }

    public void addUml2cd_operation(Uml2cd_operation uml2cd_operation) {
        this.uml2cd_operations.add(uml2cd_operation);
    }

}