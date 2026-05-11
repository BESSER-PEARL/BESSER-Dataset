





import java.util.List;
import java.util.ArrayList;

public class TypeGraphBasic_TMethodSignature extends TSignature {






    private List<TypeGraphBasic_TClass> typegraphbasic_tclasss;




    private TypeGraphBasic_TMethod typegraphbasic_tmethod;




    private TypeGraphBasic_TMethod typegraphbasic_tmethod;


    public TypeGraphBasic_TMethodSignature(
    ) {
        super(
        );
        this.typegraphbasic_tclasss = new ArrayList<>();
    }

    public TypeGraphBasic_TMethodSignature(
        ArrayList<TypeGraphBasic_TClass> typegraphbasic_tclasss    ) {
        this.typegraphbasic_tclasss = typegraphbasic_tclasss;
    }


    public List<TypeGraphBasic_TClass> getTypegraphbasic_tclasss() {
        return typegraphbasic_tclasss;
    }

    public void addTypegraphbasic_tclass(Typegraphbasic_tclass typegraphbasic_tclass) {
        this.typegraphbasic_tclasss.add(typegraphbasic_tclass);
    }
    public TypeGraphBasic_TMethod getTypegraphbasic_tmethod() {
        return typegraphbasic_tmethod;
    }

    public void setTypegraphbasic_tmethod(TypeGraphBasic_TMethod typegraphbasic_tmethod) {
        this.typegraphbasic_tmethod = typegraphbasic_tmethod;
    }
    public TypeGraphBasic_TMethod getTypegraphbasic_tmethod() {
        return typegraphbasic_tmethod;
    }

    public void setTypegraphbasic_tmethod(TypeGraphBasic_TMethod typegraphbasic_tmethod) {
        this.typegraphbasic_tmethod = typegraphbasic_tmethod;
    }

}