





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_constraints_IndexMember extends SQLObject {

    private String incrementType;



    public sqlmodel_constraints_IndexMember(
        String incrementType    ) {
        super(
        );
        this.incrementType = incrementType;
    }


    public String getIncrementtype() {
        return incrementType;
    }

    public void setIncrementtype(String incrementType) {
        this.incrementType = incrementType;
    }


}