





import java.util.List;
import java.util.ArrayList;

public class TypeGraphBasic_TypeGraph  {

    private String tName;





    private List<TypeGraphBasic_TField> typegraphbasic_tfields;




    private List<TypeGraphBasic_TMethod> typegraphbasic_tmethods;




    private List<TypeGraphBasic_TPackage> typegraphbasic_tpackages;




    private List<TypeGraphBasic_TClass> typegraphbasic_tclasss;


    public TypeGraphBasic_TypeGraph(
        String tName    ) {
        this.tName = tName;
        this.typegraphbasic_tfields = new ArrayList<>();
        this.typegraphbasic_tmethods = new ArrayList<>();
        this.typegraphbasic_tpackages = new ArrayList<>();
        this.typegraphbasic_tclasss = new ArrayList<>();
    }

    public TypeGraphBasic_TypeGraph(
        String tName        ArrayList<TypeGraphBasic_TField> typegraphbasic_tfields,        ArrayList<TypeGraphBasic_TMethod> typegraphbasic_tmethods,        ArrayList<TypeGraphBasic_TPackage> typegraphbasic_tpackages,        ArrayList<TypeGraphBasic_TClass> typegraphbasic_tclasss    ) {
        this.tName = tName;
        this.typegraphbasic_tfields = typegraphbasic_tfields;
        this.typegraphbasic_tmethods = typegraphbasic_tmethods;
        this.typegraphbasic_tpackages = typegraphbasic_tpackages;
        this.typegraphbasic_tclasss = typegraphbasic_tclasss;
    }

    public String getTname() {
        return tName;
    }

    public void setTname(String tName) {
        this.tName = tName;
    }

    public List<TypeGraphBasic_TField> getTypegraphbasic_tfields() {
        return typegraphbasic_tfields;
    }

    public void addTypegraphbasic_tfield(Typegraphbasic_tfield typegraphbasic_tfield) {
        this.typegraphbasic_tfields.add(typegraphbasic_tfield);
    }
    public List<TypeGraphBasic_TMethod> getTypegraphbasic_tmethods() {
        return typegraphbasic_tmethods;
    }

    public void addTypegraphbasic_tmethod(Typegraphbasic_tmethod typegraphbasic_tmethod) {
        this.typegraphbasic_tmethods.add(typegraphbasic_tmethod);
    }
    public List<TypeGraphBasic_TPackage> getTypegraphbasic_tpackages() {
        return typegraphbasic_tpackages;
    }

    public void addTypegraphbasic_tpackage(Typegraphbasic_tpackage typegraphbasic_tpackage) {
        this.typegraphbasic_tpackages.add(typegraphbasic_tpackage);
    }
    public List<TypeGraphBasic_TClass> getTypegraphbasic_tclasss() {
        return typegraphbasic_tclasss;
    }

    public void addTypegraphbasic_tclass(Typegraphbasic_tclass typegraphbasic_tclass) {
        this.typegraphbasic_tclasss.add(typegraphbasic_tclass);
    }

}