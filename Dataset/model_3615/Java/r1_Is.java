





import java.util.List;
import java.util.ArrayList;

public class r1_Is extends UnaryExpression {

    private String isType;



    public r1_Is(
        String isType    ) {
        super(
        );
        this.isType = isType;
    }


    public String getIstype() {
        return isType;
    }

    public void setIstype(String isType) {
        this.isType = isType;
    }


}