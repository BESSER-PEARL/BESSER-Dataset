





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_StructuredUserDefinedType extends UserDefinedType {

    private boolean instantiable;
    private boolean final;



    public sqlmodel_datatypes_StructuredUserDefinedType(
        boolean instantiable,        boolean final    ) {
        super(
        );
        this.instantiable = instantiable;
        this.final = final;
    }


    public boolean getInstantiable() {
        return instantiable;
    }

    public void setInstantiable(boolean instantiable) {
        this.instantiable = instantiable;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }


}