





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_SrcLocation extends SrcNode, SrcNodeContainer {

    private String clear;
    private String priority;
    private String url;



    public jointPackage_CPL2SPL_SrcLocation(
        String clear,        String priority,        String url    ) {
        super(
        );
        this.clear = clear;
        this.priority = priority;
        this.url = url;
    }


    public String getClear() {
        return clear;
    }

    public void setClear(String clear) {
        this.clear = clear;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}