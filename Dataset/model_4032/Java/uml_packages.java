





import java.util.List;
import java.util.ArrayList;

public class uml_packages  {

    private String group;





    private List<uml_package_> uml_package_s;




    private uml_DocumentRoot uml_documentroot;


    public uml_packages(
        String group    ) {
        this.group = group;
        this.uml_package_s = new ArrayList<>();
    }

    public uml_packages(
        String group        ArrayList<uml_package_> uml_package_s    ) {
        this.group = group;
        this.uml_package_s = uml_package_s;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<uml_package_> getUml_package_s() {
        return uml_package_s;
    }

    public void addUml_package_(Uml_package_ uml_package_) {
        this.uml_package_s.add(uml_package_);
    }
    public uml_DocumentRoot getUml_documentroot() {
        return uml_documentroot;
    }

    public void setUml_documentroot(uml_DocumentRoot uml_documentroot) {
        this.uml_documentroot = uml_documentroot;
    }

}