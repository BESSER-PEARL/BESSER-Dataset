





import java.util.List;
import java.util.ArrayList;

public class becontent_SystemAttributeVarchar extends TypedSystemAttribute {

    private int length;
    private boolean isPrimaryKey;



    public becontent_SystemAttributeVarchar(
        int length,        boolean isPrimaryKey    ) {
        super(
        );
        this.length = length;
        this.isPrimaryKey = isPrimaryKey;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public boolean getIsprimarykey() {
        return isPrimaryKey;
    }

    public void setIsprimarykey(boolean isPrimaryKey) {
        this.isPrimaryKey = isPrimaryKey;
    }


}