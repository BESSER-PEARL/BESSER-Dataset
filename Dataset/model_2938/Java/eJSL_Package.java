





import java.util.List;
import java.util.ArrayList;

public class eJSL_Package  {

    private String name;





    private eJSL_Library ejsl_library;




    private List<eJSL_Package> ejsl_packages;




    private List<eJSL_Class> ejsl_classs;


    public eJSL_Package(
        String name    ) {
        this.name = name;
        this.ejsl_packages = new ArrayList<>();
        this.ejsl_classs = new ArrayList<>();
    }

    public eJSL_Package(
        String name        ArrayList<eJSL_Package> ejsl_packages,        ArrayList<eJSL_Class> ejsl_classs    ) {
        this.name = name;
        this.ejsl_packages = ejsl_packages;
        this.ejsl_classs = ejsl_classs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eJSL_Library getEjsl_library() {
        return ejsl_library;
    }

    public void setEjsl_library(eJSL_Library ejsl_library) {
        this.ejsl_library = ejsl_library;
    }
    public List<eJSL_Package> getEjsl_packages() {
        return ejsl_packages;
    }

    public void addEjsl_package(Ejsl_package ejsl_package) {
        this.ejsl_packages.add(ejsl_package);
    }
    public List<eJSL_Class> getEjsl_classs() {
        return ejsl_classs;
    }

    public void addEjsl_class(Ejsl_class ejsl_class) {
        this.ejsl_classs.add(ejsl_class);
    }

}