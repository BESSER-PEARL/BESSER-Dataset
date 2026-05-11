





import java.util.List;
import java.util.ArrayList;

public class metrics_Measurement  {

    private String tag;
    private String name;
    private String error;



    public metrics_Measurement(
        String tag,        String name,        String error    ) {
        this.tag = tag;
        this.name = name;
        this.error = error;
    }


    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getError() {
        return error;
    }

    public void setError(String error) {
        this.error = error;
    }


}