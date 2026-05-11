





import java.util.List;
import java.util.ArrayList;

public class TypeGraphBasic_TPackage  {

    private String tName;





    private List<TypeGraphBasic_TClass> typegraphbasic_tclasss;




    private TypeGraphBasic_TPackage typegraphbasic_tpackage;




    private TypeGraphBasic_TClass typegraphbasic_tclass;




    private List<TypeGraphBasic_TPackage> typegraphbasic_tpackages;


    public TypeGraphBasic_TPackage(
        String tName    ) {
        this.tName = tName;
        this.typegraphbasic_tclasss = new ArrayList<>();
        this.typegraphbasic_tpackages = new ArrayList<>();
    }

    public TypeGraphBasic_TPackage(
        String tName        ArrayList<TypeGraphBasic_TClass> typegraphbasic_tclasss,        ArrayList<TypeGraphBasic_TPackage> typegraphbasic_tpackages    ) {
        this.tName = tName;
        this.typegraphbasic_tclasss = typegraphbasic_tclasss;
        this.typegraphbasic_tpackages = typegraphbasic_tpackages;
    }

    public String getTname() {
        return tName;
    }

    public void setTname(String tName) {
        this.tName = tName;
    }

    public List<TypeGraphBasic_TClass> getTypegraphbasic_tclasss() {
        return typegraphbasic_tclasss;
    }

    public void addTypegraphbasic_tclass(Typegraphbasic_tclass typegraphbasic_tclass) {
        this.typegraphbasic_tclasss.add(typegraphbasic_tclass);
    }
    public TypeGraphBasic_TPackage getTypegraphbasic_tpackage() {
        return typegraphbasic_tpackage;
    }

    public void setTypegraphbasic_tpackage(TypeGraphBasic_TPackage typegraphbasic_tpackage) {
        this.typegraphbasic_tpackage = typegraphbasic_tpackage;
    }
    public TypeGraphBasic_TClass getTypegraphbasic_tclass() {
        return typegraphbasic_tclass;
    }

    public void setTypegraphbasic_tclass(TypeGraphBasic_TClass typegraphbasic_tclass) {
        this.typegraphbasic_tclass = typegraphbasic_tclass;
    }
    public List<TypeGraphBasic_TPackage> getTypegraphbasic_tpackages() {
        return typegraphbasic_tpackages;
    }

    public void addTypegraphbasic_tpackage(Typegraphbasic_tpackage typegraphbasic_tpackage) {
        this.typegraphbasic_tpackages.add(typegraphbasic_tpackage);
    }

}