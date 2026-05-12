





import java.util.List;
import java.util.ArrayList;

public class dbca_Attribute extends NamedElement {

    private String type;
    private int maxLength;



    public dbca_Attribute(
        String type,        int maxLength    ) {
        super(
        );
        this.type = type;
        this.maxLength = maxLength;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(int maxLength) {
        this.maxLength = maxLength;
    }


}