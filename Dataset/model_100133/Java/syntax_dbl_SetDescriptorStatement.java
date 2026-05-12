





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_SetDescriptorStatement extends BindingStatement {

    private String descriptorName;
    private String value;



    public syntax_dbl_SetDescriptorStatement(
        String descriptorName,        String value    ) {
        super(
        );
        this.descriptorName = descriptorName;
        this.value = value;
    }


    public String getDescriptorname() {
        return descriptorName;
    }

    public void setDescriptorname(String descriptorName) {
        this.descriptorName = descriptorName;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}