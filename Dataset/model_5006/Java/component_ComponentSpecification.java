





import java.util.List;
import java.util.ArrayList;

public class component_ComponentSpecification extends Component {

    private String aliasName;
    private String rtcType;
    private boolean specUnLoad;



    public component_ComponentSpecification(
        String aliasName,        String rtcType,        boolean specUnLoad    ) {
        super(
        );
        this.aliasName = aliasName;
        this.rtcType = rtcType;
        this.specUnLoad = specUnLoad;
    }


    public String getAliasname() {
        return aliasName;
    }

    public void setAliasname(String aliasName) {
        this.aliasName = aliasName;
    }
    public String getRtctype() {
        return rtcType;
    }

    public void setRtctype(String rtcType) {
        this.rtcType = rtcType;
    }
    public boolean getSpecunload() {
        return specUnLoad;
    }

    public void setSpecunload(boolean specUnLoad) {
        this.specUnLoad = specUnLoad;
    }


}