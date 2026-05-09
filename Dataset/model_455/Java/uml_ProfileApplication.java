





import java.util.List;
import java.util.ArrayList;

public class uml_ProfileApplication extends DirectedRelationship {

    private String isStrict;



    public uml_ProfileApplication(
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