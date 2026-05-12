





import java.util.List;
import java.util.ArrayList;

public class driver_Rtest  {

    private String symbianPath;
    private String resultFile;



    public driver_Rtest(
        String symbianPath,        String resultFile    ) {
        this.symbianPath = symbianPath;
        this.resultFile = resultFile;
    }


    public String getSymbianpath() {
        return symbianPath;
    }

    public void setSymbianpath(String symbianPath) {
        this.symbianPath = symbianPath;
    }
    public String getResultfile() {
        return resultFile;
    }

    public void setResultfile(String resultFile) {
        this.resultFile = resultFile;
    }


}