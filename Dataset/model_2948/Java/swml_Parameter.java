





import java.util.List;
import java.util.ArrayList;

public class swml_Parameter  {

    private String ValueSpec;





    private swml_Link swml_link;


    public swml_Parameter(
        String ValueSpec    ) {
        this.ValueSpec = ValueSpec;
    }


    public String getValuespec() {
        return ValueSpec;
    }

    public void setValuespec(String ValueSpec) {
        this.ValueSpec = ValueSpec;
    }

    public swml_Link getSwml_link() {
        return swml_link;
    }

    public void setSwml_link(swml_Link swml_link) {
        this.swml_link = swml_link;
    }

}