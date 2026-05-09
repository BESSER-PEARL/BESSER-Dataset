





import java.util.List;
import java.util.ArrayList;

public class qvtcore_cst_DomainCS extends AreaCS {

    private boolean enforce;
    private boolean check;



    public qvtcore_cst_DomainCS(
        boolean enforce,        boolean check    ) {
        super(
        );
        this.enforce = enforce;
        this.check = check;
    }


    public boolean getEnforce() {
        return enforce;
    }

    public void setEnforce(boolean enforce) {
        this.enforce = enforce;
    }
    public boolean getCheck() {
        return check;
    }

    public void setCheck(boolean check) {
        this.check = check;
    }


}