





import java.util.List;
import java.util.ArrayList;

public class TypeGraphBasic_TMethodSignature extends TSignature {






    private TypeGraphBasic_TMethodDefinition typegraphbasic_tmethoddefinition;




    private List<TypeGraphBasic_TClass> typegraphbasic_tclasss;




    private List<TypeGraphBasic_TMethodDefinition> typegraphbasic_tmethoddefinitions;


    public TypeGraphBasic_TMethodSignature(
    ) {
        super(
        );
        this.typegraphbasic_tclasss = new ArrayList<>();
        this.typegraphbasic_tmethoddefinitions = new ArrayList<>();
    }

    public TypeGraphBasic_TMethodSignature(
        ArrayList<TypeGraphBasic_TClass> typegraphbasic_tclasss,        ArrayList<TypeGraphBasic_TMethodDefinition> typegraphbasic_tmethoddefinitions    ) {
        this.typegraphbasic_tclasss = typegraphbasic_tclasss;
        this.typegraphbasic_tmethoddefinitions = typegraphbasic_tmethoddefinitions;
    }


    public TypeGraphBasic_TMethodDefinition getTypegraphbasic_tmethoddefinition() {
        return typegraphbasic_tmethoddefinition;
    }

    public void setTypegraphbasic_tmethoddefinition(TypeGraphBasic_TMethodDefinition typegraphbasic_tmethoddefinition) {
        this.typegraphbasic_tmethoddefinition = typegraphbasic_tmethoddefinition;
    }
    public List<TypeGraphBasic_TClass> getTypegraphbasic_tclasss() {
        return typegraphbasic_tclasss;
    }

    public void addTypegraphbasic_tclass(Typegraphbasic_tclass typegraphbasic_tclass) {
        this.typegraphbasic_tclasss.add(typegraphbasic_tclass);
    }
    public List<TypeGraphBasic_TMethodDefinition> getTypegraphbasic_tmethoddefinitions() {
        return typegraphbasic_tmethoddefinitions;
    }

    public void addTypegraphbasic_tmethoddefinition(Typegraphbasic_tmethoddefinition typegraphbasic_tmethoddefinition) {
        this.typegraphbasic_tmethoddefinitions.add(typegraphbasic_tmethoddefinition);
    }

}