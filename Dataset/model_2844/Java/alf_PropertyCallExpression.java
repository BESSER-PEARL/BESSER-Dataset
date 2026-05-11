





import java.util.List;
import java.util.ArrayList;

public class alf_PropertyCallExpression extends SuffixExpression {

    private String propertyName;



    public alf_PropertyCallExpression(
        String propertyName    ) {
        super(
        );
        this.propertyName = propertyName;
    }


    public String getPropertyname() {
        return propertyName;
    }

    public void setPropertyname(String propertyName) {
        this.propertyName = propertyName;
    }


}