





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_Column extends TableProperty {

    private boolean sorted;
    private String default;



    public ddlDsl_Column(
        boolean sorted,        String default    ) {
        super(
        );
        this.sorted = sorted;
        this.default = default;
    }


    public boolean getSorted() {
        return sorted;
    }

    public void setSorted(boolean sorted) {
        this.sorted = sorted;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }


}