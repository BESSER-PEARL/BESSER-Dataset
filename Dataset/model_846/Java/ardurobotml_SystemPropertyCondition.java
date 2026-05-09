





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_SystemPropertyCondition extends Condition {

    private boolean expectedAttributeValue;



    public ardurobotml_SystemPropertyCondition(
        boolean expectedAttributeValue    ) {
        super(
        );
        this.expectedAttributeValue = expectedAttributeValue;
    }


    public boolean getExpectedattributevalue() {
        return expectedAttributeValue;
    }

    public void setExpectedattributevalue(boolean expectedAttributeValue) {
        this.expectedAttributeValue = expectedAttributeValue;
    }


}