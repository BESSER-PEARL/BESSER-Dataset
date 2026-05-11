





import java.util.List;
import java.util.ArrayList;

public class becontent_AttributeVarchar extends TypedAttribute {

    private boolean isPrimaryKey;
    private int length;



    public becontent_AttributeVarchar(
        boolean isPrimaryKey,        int length    ) {
        super(
        );
        this.isPrimaryKey = isPrimaryKey;
        this.length = length;
    }


    public boolean getIsprimarykey() {
        return isPrimaryKey;
    }

    public void setIsprimarykey(boolean isPrimaryKey) {
        this.isPrimaryKey = isPrimaryKey;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }


}