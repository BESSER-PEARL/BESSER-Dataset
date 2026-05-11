





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_TrgForeachStat extends TrgStatement {

    private String iteratorName;



    public jointPackage_CPL2SPL_TrgForeachStat(
        String iteratorName    ) {
        super(
        );
        this.iteratorName = iteratorName;
    }


    public String getIteratorname() {
        return iteratorName;
    }

    public void setIteratorname(String iteratorName) {
        this.iteratorName = iteratorName;
    }


}