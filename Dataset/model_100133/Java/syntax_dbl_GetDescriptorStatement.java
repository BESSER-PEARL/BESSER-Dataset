





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_GetDescriptorStatement extends BindingStatement {

    private String value;
    private String descriptorScope;
    private String descriptorName;



    public syntax_dbl_GetDescriptorStatement(
        String value,        String descriptorScope,        String descriptorName    ) {
        super(
        );
        this.value = value;
        this.descriptorScope = descriptorScope;
        this.descriptorName = descriptorName;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getDescriptorscope() {
        return descriptorScope;
    }

    public void setDescriptorscope(String descriptorScope) {
        this.descriptorScope = descriptorScope;
    }
    public String getDescriptorname() {
        return descriptorName;
    }

    public void setDescriptorname(String descriptorName) {
        this.descriptorName = descriptorName;
    }


}