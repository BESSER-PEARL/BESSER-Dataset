





import java.util.List;
import java.util.ArrayList;

public class workflow_Parameter  {

    private String option;
    private String data;



    public workflow_Parameter(
        String option,        String data    ) {
        this.option = option;
        this.data = data;
    }


    public String getOption() {
        return option;
    }

    public void setOption(String option) {
        this.option = option;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }


}