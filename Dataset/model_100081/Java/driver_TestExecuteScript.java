





import java.util.List;
import java.util.ArrayList;

public class driver_TestExecuteScript  {

    private String symbianPath;
    private String pCPath;





    private driver_ExecuteOnSymbian driver_executeonsymbian;


    public driver_TestExecuteScript(
        String symbianPath,        String pCPath    ) {
        this.symbianPath = symbianPath;
        this.pCPath = pCPath;
    }


    public String getSymbianpath() {
        return symbianPath;
    }

    public void setSymbianpath(String symbianPath) {
        this.symbianPath = symbianPath;
    }
    public String getPcpath() {
        return pCPath;
    }

    public void setPcpath(String pCPath) {
        this.pCPath = pCPath;
    }

    public driver_ExecuteOnSymbian getDriver_executeonsymbian() {
        return driver_executeonsymbian;
    }

    public void setDriver_executeonsymbian(driver_ExecuteOnSymbian driver_executeonsymbian) {
        this.driver_executeonsymbian = driver_executeonsymbian;
    }

}