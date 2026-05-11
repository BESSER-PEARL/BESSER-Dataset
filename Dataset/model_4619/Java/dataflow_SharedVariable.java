





import java.util.List;
import java.util.ArrayList;

public class dataflow_SharedVariable extends Variable {

    private String tag;



    public dataflow_SharedVariable(
        String tag    ) {
        super(
        );
        this.tag = tag;
    }


    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }


}