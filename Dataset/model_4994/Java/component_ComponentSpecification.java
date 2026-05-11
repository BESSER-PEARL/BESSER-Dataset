





import java.util.List;
import java.util.ArrayList;

public class component_ComponentSpecification extends Component {

    private String aliasName;
    private boolean specUnLoad;
    private String rtcType;



    public component_ComponentSpecification(
        String aliasName,        boolean specUnLoad,        String rtcType    ) {
        super(
        );
        this.aliasName = aliasName;
        this.specUnLoad = specUnLoad;
        this.rtcType = rtcType;
    }


    public String getAliasname() {
        return aliasName;
    }

    public void setAliasname(String aliasName) {
        this.aliasName = aliasName;
    }
    public boolean getSpecunload() {
        return specUnLoad;
    }

    public void setSpecunload(boolean specUnLoad) {
        this.specUnLoad = specUnLoad;
    }
    public String getRtctype() {
        return rtcType;
    }

    public void setRtctype(String rtcType) {
        this.rtcType = rtcType;
    }


}