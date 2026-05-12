





import java.util.List;
import java.util.ArrayList;

public class driver_Transfer  {

    private String pCPath;
    private String symbianPath;
    private String move;





    private driver_RetrieveFromSymbian driver_retrievefromsymbian;


    public driver_Transfer(
        String pCPath,        String symbianPath,        String move    ) {
        this.pCPath = pCPath;
        this.symbianPath = symbianPath;
        this.move = move;
    }


    public String getPcpath() {
        return pCPath;
    }

    public void setPcpath(String pCPath) {
        this.pCPath = pCPath;
    }
    public String getSymbianpath() {
        return symbianPath;
    }

    public void setSymbianpath(String symbianPath) {
        this.symbianPath = symbianPath;
    }
    public String getMove() {
        return move;
    }

    public void setMove(String move) {
        this.move = move;
    }

    public driver_RetrieveFromSymbian getDriver_retrievefromsymbian() {
        return driver_retrievefromsymbian;
    }

    public void setDriver_retrievefromsymbian(driver_RetrieveFromSymbian driver_retrievefromsymbian) {
        this.driver_retrievefromsymbian = driver_retrievefromsymbian;
    }

}