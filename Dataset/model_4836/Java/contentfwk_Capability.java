





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Capability extends Element {

    private String increments;
    private String businessValue;





    private contentfwk_StrategicArchitecture contentfwk_strategicarchitecture;


    public contentfwk_Capability(
        String increments,        String businessValue    ) {
        super(
        );
        this.increments = increments;
        this.businessValue = businessValue;
    }


    public String getIncrements() {
        return increments;
    }

    public void setIncrements(String increments) {
        this.increments = increments;
    }
    public String getBusinessvalue() {
        return businessValue;
    }

    public void setBusinessvalue(String businessValue) {
        this.businessValue = businessValue;
    }

    public contentfwk_StrategicArchitecture getContentfwk_strategicarchitecture() {
        return contentfwk_strategicarchitecture;
    }

    public void setContentfwk_strategicarchitecture(contentfwk_StrategicArchitecture contentfwk_strategicarchitecture) {
        this.contentfwk_strategicarchitecture = contentfwk_strategicarchitecture;
    }

}