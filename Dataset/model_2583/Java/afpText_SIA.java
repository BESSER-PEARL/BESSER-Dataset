





import java.util.List;
import java.util.ArrayList;

public class afpText_SIA extends triplet {

    private String ADJSTMNT;
    private String DIRCTION;



    public afpText_SIA(
        String ADJSTMNT,        String DIRCTION    ) {
        super(
        );
        this.ADJSTMNT = ADJSTMNT;
        this.DIRCTION = DIRCTION;
    }


    public String getAdjstmnt() {
        return ADJSTMNT;
    }

    public void setAdjstmnt(String ADJSTMNT) {
        this.ADJSTMNT = ADJSTMNT;
    }
    public String getDirction() {
        return DIRCTION;
    }

    public void setDirction(String DIRCTION) {
        this.DIRCTION = DIRCTION;
    }


}