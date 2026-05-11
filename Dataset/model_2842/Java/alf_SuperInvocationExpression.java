





import java.util.List;
import java.util.ArrayList;

public class alf_SuperInvocationExpression extends ValueSpecification, NonLiteralValueSpecification {

    private String className;



    public alf_SuperInvocationExpression(
        String className    ) {
        super(
        );
        this.className = className;
    }


    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }


}