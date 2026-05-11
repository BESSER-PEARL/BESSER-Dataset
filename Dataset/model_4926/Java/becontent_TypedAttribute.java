





import java.util.List;
import java.util.ArrayList;

public class becontent_TypedAttribute extends EntityField {

    private boolean isMandatory;
    private String name;



    public becontent_TypedAttribute(
        boolean isMandatory,        String name    ) {
        super(
        );
        this.isMandatory = isMandatory;
        this.name = name;
    }


    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}