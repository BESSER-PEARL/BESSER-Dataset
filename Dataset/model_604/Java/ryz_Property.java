





import java.util.List;
import java.util.ArrayList;

public class ryz_Property extends NamedElement {

    private boolean isRequired;
    private String type;



    public ryz_Property(
        boolean isRequired,        String type    ) {
        super(
        );
        this.isRequired = isRequired;
        this.type = type;
    }


    public boolean getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(boolean isRequired) {
        this.isRequired = isRequired;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}