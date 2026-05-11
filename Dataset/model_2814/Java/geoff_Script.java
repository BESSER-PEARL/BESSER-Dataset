





import java.util.List;
import java.util.ArrayList;

public class geoff_Script extends Identifiable {

    private String type;
    private String src;
    private String context;



    public geoff_Script(
        String type,        String src,        String context    ) {
        super(
        );
        this.type = type;
        this.src = src;
        this.context = context;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }


}