





import java.util.List;
import java.util.ArrayList;

public class express_core_DomainRule extends core_DomainConstraint, core_TypeElement {

    private String position;



    public express_core_DomainRule(
        String position    ) {
        super(
        );
        this.position = position;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }


}