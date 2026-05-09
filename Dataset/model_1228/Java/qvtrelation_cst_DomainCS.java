





import java.util.List;
import java.util.ArrayList;

public class qvtrelation_cst_DomainCS extends AbstractDomainCS {

    private boolean replace;
    private boolean checkonly;
    private boolean enforce;



    public qvtrelation_cst_DomainCS(
        boolean replace,        boolean checkonly,        boolean enforce    ) {
        super(
        );
        this.replace = replace;
        this.checkonly = checkonly;
        this.enforce = enforce;
    }


    public boolean getReplace() {
        return replace;
    }

    public void setReplace(boolean replace) {
        this.replace = replace;
    }
    public boolean getCheckonly() {
        return checkonly;
    }

    public void setCheckonly(boolean checkonly) {
        this.checkonly = checkonly;
    }
    public boolean getEnforce() {
        return enforce;
    }

    public void setEnforce(boolean enforce) {
        this.enforce = enforce;
    }


}