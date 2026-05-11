





import java.util.List;
import java.util.ArrayList;

public class model_AccessRelationship extends Relationship {

    private int accessType;



    public model_AccessRelationship(
        int accessType    ) {
        super(
        );
        this.accessType = accessType;
    }


    public int getAccesstype() {
        return accessType;
    }

    public void setAccesstype(int accessType) {
        this.accessType = accessType;
    }


}