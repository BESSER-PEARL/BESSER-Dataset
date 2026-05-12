





import java.util.List;
import java.util.ArrayList;

public class build_command_FilterAdvice extends IAdvise {

    private String filterOp;



    public build_command_FilterAdvice(
        String filterOp    ) {
        super(
        );
        this.filterOp = filterOp;
    }


    public String getFilterop() {
        return filterOp;
    }

    public void setFilterop(String filterOp) {
        this.filterOp = filterOp;
    }


}