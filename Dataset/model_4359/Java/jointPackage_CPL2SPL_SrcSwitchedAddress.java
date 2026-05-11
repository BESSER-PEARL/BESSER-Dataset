





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_SrcSwitchedAddress extends SrcNodeContainer {

    private String is_;
    private String subDomainOf;
    private String contains;



    public jointPackage_CPL2SPL_SrcSwitchedAddress(
        String is_,        String subDomainOf,        String contains    ) {
        super(
        );
        this.is_ = is_;
        this.subDomainOf = subDomainOf;
        this.contains = contains;
    }


    public String getIs_() {
        return is_;
    }

    public void setIs_(String is_) {
        this.is_ = is_;
    }
    public String getSubdomainof() {
        return subDomainOf;
    }

    public void setSubdomainof(String subDomainOf) {
        this.subDomainOf = subDomainOf;
    }
    public String getContains() {
        return contains;
    }

    public void setContains(String contains) {
        this.contains = contains;
    }


}