





import java.util.List;
import java.util.ArrayList;

public class TypeGraphBasic_TMethod  {

    private String tName;





    private List<TypeGraphBasic_TMethodSignature> typegraphbasic_tmethodsignatures;




    private TypeGraphBasic_TMethodSignature typegraphbasic_tmethodsignature;


    public TypeGraphBasic_TMethod(
        String tName    ) {
        this.tName = tName;
        this.typegraphbasic_tmethodsignatures = new ArrayList<>();
    }

    public TypeGraphBasic_TMethod(
        String tName        ArrayList<TypeGraphBasic_TMethodSignature> typegraphbasic_tmethodsignatures    ) {
        this.tName = tName;
        this.typegraphbasic_tmethodsignatures = typegraphbasic_tmethodsignatures;
    }

    public String getTname() {
        return tName;
    }

    public void setTname(String tName) {
        this.tName = tName;
    }

    public List<TypeGraphBasic_TMethodSignature> getTypegraphbasic_tmethodsignatures() {
        return typegraphbasic_tmethodsignatures;
    }

    public void addTypegraphbasic_tmethodsignature(Typegraphbasic_tmethodsignature typegraphbasic_tmethodsignature) {
        this.typegraphbasic_tmethodsignatures.add(typegraphbasic_tmethodsignature);
    }
    public TypeGraphBasic_TMethodSignature getTypegraphbasic_tmethodsignature() {
        return typegraphbasic_tmethodsignature;
    }

    public void setTypegraphbasic_tmethodsignature(TypeGraphBasic_TMethodSignature typegraphbasic_tmethodsignature) {
        this.typegraphbasic_tmethodsignature = typegraphbasic_tmethodsignature;
    }

}