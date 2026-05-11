





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Capability extends Element {

    private String businessValue;
    private String increments;





    private contentfwk_StrategicArchitecture contentfwk_strategicarchitecture;


    public contentfwk_Capability(
        String businessValue,        String increments    ) {
        super(
        );
        this.businessValue = businessValue;
        this.increments = increments;
    }


    public String getBusinessvalue() {
        return businessValue;
    }

    public void setBusinessvalue(String businessValue) {
        this.businessValue = businessValue;
    }
    public String getIncrements() {
        return increments;
    }

    public void setIncrements(String increments) {
        this.increments = increments;
    }

    public contentfwk_StrategicArchitecture getContentfwk_strategicarchitecture() {
        return contentfwk_strategicarchitecture;
    }

    public void setContentfwk_strategicarchitecture(contentfwk_StrategicArchitecture contentfwk_strategicarchitecture) {
        this.contentfwk_strategicarchitecture = contentfwk_strategicarchitecture;
    }

}