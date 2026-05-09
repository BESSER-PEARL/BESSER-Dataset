





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_MappingCallExp extends ImperativeCallExp {

    private String isStrict;



    public FlatQVT_MappingCallExp(
        String isStrict    ) {
        super(
        );
        this.isStrict = isStrict;
    }


    public String getIsstrict() {
        return isStrict;
    }

    public void setIsstrict(String isStrict) {
        this.isStrict = isStrict;
    }


}