





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedPackage extends uml_TracedPackageableElement, uml_TracedTemplateableElement, uml_TracedNamespace {






    private uml_TracedPackage uml_tracedpackage;




    private List<uml_TracedPackage> uml_tracedpackages;




    private List<uml_TracedPackageMerge> uml_tracedpackagemerges;




    private List<uml_TracedStereotype> uml_tracedstereotypes;




    private List<uml_TracedProfileApplication> uml_tracedprofileapplications;


    public umlTrace_uml_TracedPackage(
    ) {
        super(
        );
        this.uml_tracedpackages = new ArrayList<>();
        this.uml_tracedpackagemerges = new ArrayList<>();
        this.uml_tracedstereotypes = new ArrayList<>();
        this.uml_tracedprofileapplications = new ArrayList<>();
    }

    public umlTrace_uml_TracedPackage(
        ArrayList<uml_TracedPackage> uml_tracedpackages,        ArrayList<uml_TracedPackageMerge> uml_tracedpackagemerges,        ArrayList<uml_TracedStereotype> uml_tracedstereotypes,        ArrayList<uml_TracedProfileApplication> uml_tracedprofileapplications    ) {
        this.uml_tracedpackages = uml_tracedpackages;
        this.uml_tracedpackagemerges = uml_tracedpackagemerges;
        this.uml_tracedstereotypes = uml_tracedstereotypes;
        this.uml_tracedprofileapplications = uml_tracedprofileapplications;
    }


    public uml_TracedPackage getUml_tracedpackage() {
        return uml_tracedpackage;
    }

    public void setUml_tracedpackage(uml_TracedPackage uml_tracedpackage) {
        this.uml_tracedpackage = uml_tracedpackage;
    }
    public List<uml_TracedPackage> getUml_tracedpackages() {
        return uml_tracedpackages;
    }

    public void addUml_tracedpackage(Uml_tracedpackage uml_tracedpackage) {
        this.uml_tracedpackages.add(uml_tracedpackage);
    }
    public List<uml_TracedPackageMerge> getUml_tracedpackagemerges() {
        return uml_tracedpackagemerges;
    }

    public void addUml_tracedpackagemerge(Uml_tracedpackagemerge uml_tracedpackagemerge) {
        this.uml_tracedpackagemerges.add(uml_tracedpackagemerge);
    }
    public List<uml_TracedStereotype> getUml_tracedstereotypes() {
        return uml_tracedstereotypes;
    }

    public void addUml_tracedstereotype(Uml_tracedstereotype uml_tracedstereotype) {
        this.uml_tracedstereotypes.add(uml_tracedstereotype);
    }
    public List<uml_TracedProfileApplication> getUml_tracedprofileapplications() {
        return uml_tracedprofileapplications;
    }

    public void addUml_tracedprofileapplication(Uml_tracedprofileapplication uml_tracedprofileapplication) {
        this.uml_tracedprofileapplications.add(uml_tracedprofileapplication);
    }

}