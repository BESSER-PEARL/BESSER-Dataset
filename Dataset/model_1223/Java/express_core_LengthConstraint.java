





import java.util.List;
import java.util.ArrayList;

public class express_core_LengthConstraint extends DomainConstraint {

    private String isFixed;
    private String maxLength;



    public express_core_LengthConstraint(
        String isFixed,        String maxLength    ) {
        super(
        );
        this.isFixed = isFixed;
        this.maxLength = maxLength;
    }


    public String getIsfixed() {
        return isFixed;
    }

    public void setIsfixed(String isFixed) {
        this.isFixed = isFixed;
    }
    public String getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(String maxLength) {
        this.maxLength = maxLength;
    }


}