





import java.util.List;
import java.util.ArrayList;

public class art_type_Port extends CardinalityElement, type_AbstractPort {

    private String isOptional;



    public art_type_Port(
        String isOptional    ) {
        super(
        );
        this.isOptional = isOptional;
    }


    public String getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(String isOptional) {
        this.isOptional = isOptional;
    }


}