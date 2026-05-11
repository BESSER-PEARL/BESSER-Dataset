





import java.util.List;
import java.util.ArrayList;

public class ramRoot_MTpos__Chair extends MTpos__Element {

    private String MTpos__order;





    private ramRoot_MTpos__Table ramroot_mtpos__table;


    public ramRoot_MTpos__Chair(
        String MTpos__order    ) {
        super(
        );
        this.MTpos__order = MTpos__order;
    }


    public String getMtpos__order() {
        return MTpos__order;
    }

    public void setMtpos__order(String MTpos__order) {
        this.MTpos__order = MTpos__order;
    }

    public ramRoot_MTpos__Table getRamroot_mtpos__table() {
        return ramroot_mtpos__table;
    }

    public void setRamroot_mtpos__table(ramRoot_MTpos__Table ramroot_mtpos__table) {
        this.ramroot_mtpos__table = ramroot_mtpos__table;
    }

}