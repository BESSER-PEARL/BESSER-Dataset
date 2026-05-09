





import java.util.List;
import java.util.ArrayList;

public class express_core_SizeConstraint extends DomainConstraint {

    private String bound;



    public express_core_SizeConstraint(
        String bound    ) {
        super(
        );
        this.bound = bound;
    }


    public String getBound() {
        return bound;
    }

    public void setBound(String bound) {
        this.bound = bound;
    }


}