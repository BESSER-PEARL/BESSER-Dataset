





import java.util.List;
import java.util.ArrayList;

public class AsmL_Method extends Function, VarOrMethod {

    private String isOverride;
    private String isEntryPoint;
    private String isShared;
    private String isAbstract;



    public AsmL_Method(
        String isOverride,        String isEntryPoint,        String isShared,        String isAbstract    ) {
        super(
        );
        this.isOverride = isOverride;
        this.isEntryPoint = isEntryPoint;
        this.isShared = isShared;
        this.isAbstract = isAbstract;
    }


    public String getIsoverride() {
        return isOverride;
    }

    public void setIsoverride(String isOverride) {
        this.isOverride = isOverride;
    }
    public String getIsentrypoint() {
        return isEntryPoint;
    }

    public void setIsentrypoint(String isEntryPoint) {
        this.isEntryPoint = isEntryPoint;
    }
    public String getIsshared() {
        return isShared;
    }

    public void setIsshared(String isShared) {
        this.isShared = isShared;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }


}