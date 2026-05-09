





import java.util.List;
import java.util.ArrayList;

public class uml_Package extends Namespace, PackageableElement, TemplateableElement {






    private uml_PackageMerge uml_packagemerge;




    private uml_Package uml_package;




    private uml_ProfileApplication uml_profileapplication;




    private List<uml_Package> uml_packages;




    private List<uml_ProfileApplication> uml_profileapplications;




    private uml_PackageImport uml_packageimport;




    private List<uml_PackageMerge> uml_packagemerges;




    private uml_PackageMerge uml_packagemerge;


    public uml_Package(
    ) {
        super(
        );
        this.uml_packages = new ArrayList<>();
        this.uml_profileapplications = new ArrayList<>();
        this.uml_packagemerges = new ArrayList<>();
    }

    public uml_Package(
        ArrayList<uml_Package> uml_packages,        ArrayList<uml_ProfileApplication> uml_profileapplications,        ArrayList<uml_PackageMerge> uml_packagemerges    ) {
        this.uml_packages = uml_packages;
        this.uml_profileapplications = uml_profileapplications;
        this.uml_packagemerges = uml_packagemerges;
    }


    public uml_PackageMerge getUml_packagemerge() {
        return uml_packagemerge;
    }

    public void setUml_packagemerge(uml_PackageMerge uml_packagemerge) {
        this.uml_packagemerge = uml_packagemerge;
    }
    public uml_Package getUml_package() {
        return uml_package;
    }

    public void setUml_package(uml_Package uml_package) {
        this.uml_package = uml_package;
    }
    public uml_ProfileApplication getUml_profileapplication() {
        return uml_profileapplication;
    }

    public void setUml_profileapplication(uml_ProfileApplication uml_profileapplication) {
        this.uml_profileapplication = uml_profileapplication;
    }
    public List<uml_Package> getUml_packages() {
        return uml_packages;
    }

    public void addUml_package(Uml_package uml_package) {
        this.uml_packages.add(uml_package);
    }
    public List<uml_ProfileApplication> getUml_profileapplications() {
        return uml_profileapplications;
    }

    public void addUml_profileapplication(Uml_profileapplication uml_profileapplication) {
        this.uml_profileapplications.add(uml_profileapplication);
    }
    public uml_PackageImport getUml_packageimport() {
        return uml_packageimport;
    }

    public void setUml_packageimport(uml_PackageImport uml_packageimport) {
        this.uml_packageimport = uml_packageimport;
    }
    public List<uml_PackageMerge> getUml_packagemerges() {
        return uml_packagemerges;
    }

    public void addUml_packagemerge(Uml_packagemerge uml_packagemerge) {
        this.uml_packagemerges.add(uml_packagemerge);
    }
    public uml_PackageMerge getUml_packagemerge() {
        return uml_packagemerge;
    }

    public void setUml_packagemerge(uml_PackageMerge uml_packagemerge) {
        this.uml_packagemerge = uml_packagemerge;
    }

}