





import java.util.List;
import java.util.ArrayList;

public class r2_TEL extends ANY {

    private String capabilities;
    private String use;
    private String value;



    public r2_TEL(
        String capabilities,        String use,        String value    ) {
        super(
        );
        this.capabilities = capabilities;
        this.use = use;
        this.value = value;
    }


    public String getCapabilities() {
        return capabilities;
    }

    public void setCapabilities(String capabilities) {
        this.capabilities = capabilities;
    }
    public String getUse() {
        return use;
    }

    public void setUse(String use) {
        this.use = use;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}