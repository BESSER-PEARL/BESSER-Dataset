





import java.util.List;
import java.util.ArrayList;

public class becontent_SystemAttributeInteger extends TypedSystemAttribute {

    private boolean isPrimaryKey;



    public becontent_SystemAttributeInteger(
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