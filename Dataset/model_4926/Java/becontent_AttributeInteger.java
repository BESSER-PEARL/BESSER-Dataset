





import java.util.List;
import java.util.ArrayList;

public class becontent_AttributeInteger extends TypedAttribute {

    private boolean isPrimaryKey;



    public becontent_AttributeInteger(
        boolean isPrimaryKey    ) {
        super(
        );
        this.isPrimaryKey = isPrimaryKey;
    }


    public boolean getIsprimarykey() {
        return isPrimaryKey;
    }

    public void setIsprimarykey(boolean isPrimaryKey) {
        this.isPrimaryKey = isPrimaryKey;
    }


}