





import java.util.List;
import java.util.ArrayList;

public class model_base_IExternal  {

    private String source;
    private String extId2;
    private boolean live;
    private String extId;



    public model_base_IExternal(
        String source,        String extId2,        boolean live,        String extId    ) {
        this.source = source;
        this.extId2 = extId2;
        this.live = live;
        this.extId = extId;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getExtid2() {
        return extId2;
    }

    public void setExtid2(String extId2) {
        this.extId2 = extId2;
    }
    public boolean getLive() {
        return live;
    }

    public void setLive(boolean live) {
        this.live = live;
    }
    public String getExtid() {
        return extId;
    }

    public void setExtid(String extId) {
        this.extId = extId;
    }


}