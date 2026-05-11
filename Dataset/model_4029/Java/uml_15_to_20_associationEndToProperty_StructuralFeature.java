





import java.util.List;
import java.util.ArrayList;

public class uml_15_to_20_associationEndToProperty_StructuralFeature  {

    private String ownerScope;
    private String targetScope;





    private uml_15_to_20_associationEndToProperty_Class uml_15_to_20_associationendtoproperty_class;


    public uml_15_to_20_associationEndToProperty_StructuralFeature(
        String ownerScope,        String targetScope    ) {
        this.ownerScope = ownerScope;
        this.targetScope = targetScope;
    }


    public String getOwnerscope() {
        return ownerScope;
    }

    public void setOwnerscope(String ownerScope) {
        this.ownerScope = ownerScope;
    }
    public String getTargetscope() {
        return targetScope;
    }

    public void setTargetscope(String targetScope) {
        this.targetScope = targetScope;
    }

    public uml_15_to_20_associationEndToProperty_Class getUml_15_to_20_associationendtoproperty_class() {
        return uml_15_to_20_associationendtoproperty_class;
    }

    public void setUml_15_to_20_associationendtoproperty_class(uml_15_to_20_associationEndToProperty_Class uml_15_to_20_associationendtoproperty_class) {
        this.uml_15_to_20_associationendtoproperty_class = uml_15_to_20_associationendtoproperty_class;
    }

}