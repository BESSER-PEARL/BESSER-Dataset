





import java.util.List;
import java.util.ArrayList;

public class vcml_ObjectType  {

    private int classType;
    private String type;





    private vcml_ConstraintMaterial vcml_constraintmaterial;


    public vcml_ObjectType(
        int classType,        String type    ) {
        this.classType = classType;
        this.type = type;
    }


    public int getClasstype() {
        return classType;
    }

    public void setClasstype(int classType) {
        this.classType = classType;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public vcml_ConstraintMaterial getVcml_constraintmaterial() {
        return vcml_constraintmaterial;
    }

    public void setVcml_constraintmaterial(vcml_ConstraintMaterial vcml_constraintmaterial) {
        this.vcml_constraintmaterial = vcml_constraintmaterial;
    }

}