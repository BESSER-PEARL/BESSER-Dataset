





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_UploadCommand  {

    private String source;
    private String target;



    public cloudml_core_UploadCommand(
        String source,        String target    ) {
        this.source = source;
        this.target = target;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }


}