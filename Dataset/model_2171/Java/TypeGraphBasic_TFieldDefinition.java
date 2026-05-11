





import java.util.List;
import java.util.ArrayList;

public class TypeGraphBasic_TFieldDefinition extends TMember {






    private TypeGraphBasic_TFieldSignature typegraphbasic_tfieldsignature;




    private List<TypeGraphBasic_TFieldDefinition> typegraphbasic_tfielddefinitions;




    private TypeGraphBasic_TFieldSignature typegraphbasic_tfieldsignature;




    private TypeGraphBasic_TFieldDefinition typegraphbasic_tfielddefinition;


    public TypeGraphBasic_TFieldDefinition(
    ) {
        super(
        );
        this.typegraphbasic_tfielddefinitions = new ArrayList<>();
    }

    public TypeGraphBasic_TFieldDefinition(
        ArrayList<TypeGraphBasic_TFieldDefinition> typegraphbasic_tfielddefinitions    ) {
        this.typegraphbasic_tfielddefinitions = typegraphbasic_tfielddefinitions;
    }


    public TypeGraphBasic_TFieldSignature getTypegraphbasic_tfieldsignature() {
        return typegraphbasic_tfieldsignature;
    }

    public void setTypegraphbasic_tfieldsignature(TypeGraphBasic_TFieldSignature typegraphbasic_tfieldsignature) {
        this.typegraphbasic_tfieldsignature = typegraphbasic_tfieldsignature;
    }
    public List<TypeGraphBasic_TFieldDefinition> getTypegraphbasic_tfielddefinitions() {
        return typegraphbasic_tfielddefinitions;
    }

    public void addTypegraphbasic_tfielddefinition(Typegraphbasic_tfielddefinition typegraphbasic_tfielddefinition) {
        this.typegraphbasic_tfielddefinitions.add(typegraphbasic_tfielddefinition);
    }
    public TypeGraphBasic_TFieldSignature getTypegraphbasic_tfieldsignature() {
        return typegraphbasic_tfieldsignature;
    }

    public void setTypegraphbasic_tfieldsignature(TypeGraphBasic_TFieldSignature typegraphbasic_tfieldsignature) {
        this.typegraphbasic_tfieldsignature = typegraphbasic_tfieldsignature;
    }
    public TypeGraphBasic_TFieldDefinition getTypegraphbasic_tfielddefinition() {
        return typegraphbasic_tfielddefinition;
    }

    public void setTypegraphbasic_tfielddefinition(TypeGraphBasic_TFieldDefinition typegraphbasic_tfielddefinition) {
        this.typegraphbasic_tfielddefinition = typegraphbasic_tfielddefinition;
    }

}