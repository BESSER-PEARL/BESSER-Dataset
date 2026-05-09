





import java.util.List;
import java.util.ArrayList;

public class ryz_TableKey extends NamedElement {

    private boolean isRequired;
    private boolean isPrimaryKey;
    private String type;
    private boolean isForeignKey;



    public ryz_TableKey(
        boolean isRequired,        boolean isPrimaryKey,        String type,        boolean isForeignKey    ) {
        super(
        );
        this.isRequired = isRequired;
        this.isPrimaryKey = isPrimaryKey;
        this.type = type;
        this.isForeignKey = isForeignKey;
    }


    public boolean getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(boolean isRequired) {
        this.isRequired = isRequired;
    }
    public boolean getIsprimarykey() {
        return isPrimaryKey;
    }

    public void setIsprimarykey(boolean isPrimaryKey) {
        this.isPrimaryKey = isPrimaryKey;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getIsforeignkey() {
        return isForeignKey;
    }

    public void setIsforeignkey(boolean isForeignKey) {
        this.isForeignKey = isForeignKey;
    }


}