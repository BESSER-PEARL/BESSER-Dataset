





import java.util.List;
import java.util.ArrayList;

public class afpText_TBM extends triplet {

    private String PRECSION;
    private String DIRCTION;
    private String INCRMENT;



    public afpText_TBM(
        String PRECSION,        String DIRCTION,        String INCRMENT    ) {
        super(
        );
        this.PRECSION = PRECSION;
        this.DIRCTION = DIRCTION;
        this.INCRMENT = INCRMENT;
    }


    public String getPrecsion() {
        return PRECSION;
    }

    public void setPrecsion(String PRECSION) {
        this.PRECSION = PRECSION;
    }
    public String getDirction() {
        return DIRCTION;
    }

    public void setDirction(String DIRCTION) {
        this.DIRCTION = DIRCTION;
    }
    public String getIncrment() {
        return INCRMENT;
    }

    public void setIncrment(String INCRMENT) {
        this.INCRMENT = INCRMENT;
    }


}