





import java.util.List;
import java.util.ArrayList;

public class model_testspecification_TestProcedure extends base_IContainer, base_IExternal {

    private boolean isRegressionTest;



    public model_testspecification_TestProcedure(
        boolean isRegressionTest    ) {
        super(
        );
        this.isRegressionTest = isRegressionTest;
    }


    public boolean getIsregressiontest() {
        return isRegressionTest;
    }

    public void setIsregressiontest(boolean isRegressionTest) {
        this.isRegressionTest = isRegressionTest;
    }


}