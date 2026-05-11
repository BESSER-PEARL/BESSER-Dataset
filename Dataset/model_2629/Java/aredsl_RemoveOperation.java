





import java.util.List;
import java.util.ArrayList;

public class aredsl_RemoveOperation extends DomainOperation {

    private String constraint;



    public aredsl_RemoveOperation(
        String constraint    ) {
        super(
        );
        this.constraint = constraint;
    }


    public String getConstraint() {
        return constraint;
    }

    public void setConstraint(String constraint) {
        this.constraint = constraint;
    }


}