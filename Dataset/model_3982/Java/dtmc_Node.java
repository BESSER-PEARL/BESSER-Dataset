





import java.util.List;
import java.util.ArrayList;

public class dtmc_Node  {

    private boolean isFail;
    private boolean isStart;
    private boolean isEnd;



    public dtmc_Node(
        boolean isFail,        boolean isStart,        boolean isEnd    ) {
        this.isFail = isFail;
        this.isStart = isStart;
        this.isEnd = isEnd;
    }


    public boolean getIsfail() {
        return isFail;
    }

    public void setIsfail(boolean isFail) {
        this.isFail = isFail;
    }
    public boolean getIsstart() {
        return isStart;
    }

    public void setIsstart(boolean isStart) {
        this.isStart = isStart;
    }
    public boolean getIsend() {
        return isEnd;
    }

    public void setIsend(boolean isEnd) {
        this.isEnd = isEnd;
    }


}