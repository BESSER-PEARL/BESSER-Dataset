





import java.util.List;
import java.util.ArrayList;

public class TypeGraphBasic_TClass  {

    private String tName;





    private List<TypeGraphBasic_TClass> typegraphbasic_tclasss;




    private TypeGraphBasic_TClass typegraphbasic_tclass;


    public TypeGraphBasic_TClass(
        String tName    ) {
        this.tName = tName;
        this.typegraphbasic_tclasss = new ArrayList<>();
    }

    public TypeGraphBasic_TClass(
        String tName        ArrayList<TypeGraphBasic_TClass> typegraphbasic_tclasss    ) {
        this.tName = tName;
        this.typegraphbasic_tclasss = typegraphbasic_tclasss;
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
    public TypeGraphBasic_TClass getTypegraphbasic_tclass() {
        return typegraphbasic_tclass;
    }

    public void setTypegraphbasic_tclass(TypeGraphBasic_TClass typegraphbasic_tclass) {
        this.typegraphbasic_tclass = typegraphbasic_tclass;
    }

}