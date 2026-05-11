





import java.util.List;
import java.util.ArrayList;

public class psample_Variable extends Member {

    private boolean isParameter;





    private psample_Function psample_function;


    public psample_Variable(
        boolean isParameter    ) {
        super(
        );
        this.isParameter = isParameter;
    }


    public boolean getIsparameter() {
        return isParameter;
    }

    public void setIsparameter(boolean isParameter) {
        this.isParameter = isParameter;
    }

    public psample_Function getPsample_function() {
        return psample_function;
    }

    public void setPsample_function(psample_Function psample_function) {
        this.psample_function = psample_function;
    }

}