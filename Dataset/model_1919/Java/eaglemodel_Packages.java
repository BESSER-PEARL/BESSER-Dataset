





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Packages  {






    private List<eaglemodel_Package> eaglemodel_packages;




    private eaglemodel_Library eaglemodel_library;


    public eaglemodel_Packages(
    ) {
        this.eaglemodel_packages = new ArrayList<>();
    }

    public eaglemodel_Packages(
        ArrayList<eaglemodel_Package> eaglemodel_packages    ) {
        this.eaglemodel_packages = eaglemodel_packages;
    }


    public List<eaglemodel_Package> getEaglemodel_packages() {
        return eaglemodel_packages;
    }

    public void addEaglemodel_package(Eaglemodel_package eaglemodel_package) {
        this.eaglemodel_packages.add(eaglemodel_package);
    }
    public eaglemodel_Library getEaglemodel_library() {
        return eaglemodel_library;
    }

    public void setEaglemodel_library(eaglemodel_Library eaglemodel_library) {
        this.eaglemodel_library = eaglemodel_library;
    }

}