





import java.util.List;
import java.util.ArrayList;

public class afpText_PagePositionInformation extends triplet {

    private String PGPRG;



    public afpText_PagePositionInformation(
        String PGPRG    ) {
        super(
        );
        this.PGPRG = PGPRG;
    }


    public String getPgprg() {
        return PGPRG;
    }

    public void setPgprg(String PGPRG) {
        this.PGPRG = PGPRG;
    }


}