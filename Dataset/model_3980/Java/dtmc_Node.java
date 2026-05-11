





import java.util.List;
import java.util.ArrayList;

public class dtmc_Node extends NamedEntity {

    private boolean isEnd;
    private boolean isFail;
    private boolean isStart;





    private dtmc_Module dtmc_module;




    private dtmc_Module dtmc_module;


    public dtmc_Node(
        boolean isEnd,        boolean isFail,        boolean isStart    ) {
        super(
        );
        this.isEnd = isEnd;
        this.isFail = isFail;
        this.isStart = isStart;
    }


    public boolean getIsend() {
        return isEnd;
    }

    public void setIsend(boolean isEnd) {
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

    public dtmc_Module getDtmc_module() {
        return dtmc_module;
    }

    public void setDtmc_module(dtmc_Module dtmc_module) {
        this.dtmc_module = dtmc_module;
    }
    public dtmc_Module getDtmc_module() {
        return dtmc_module;
    }

    public void setDtmc_module(dtmc_Module dtmc_module) {
        this.dtmc_module = dtmc_module;
    }

}