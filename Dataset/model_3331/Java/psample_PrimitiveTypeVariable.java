





import java.util.List;
import java.util.ArrayList;

public class psample_PrimitiveTypeVariable extends Type {

    private boolean isParameter;





    private psample_Class psample_class;


    public psample_PrimitiveTypeVariable(
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

    public psample_Class getPsample_class() {
        return psample_class;
    }

    public void setPsample_class(psample_Class psample_class) {
        this.psample_class = psample_class;
    }

}