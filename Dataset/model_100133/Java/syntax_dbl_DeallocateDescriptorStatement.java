





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_DeallocateDescriptorStatement extends BindingStatement {

    private String descriptorName;
    private String descriptorScope;



    public syntax_dbl_DeallocateDescriptorStatement(
        String descriptorName,        String descriptorScope    ) {
        super(
        );
        this.descriptorName = descriptorName;
        this.descriptorScope = descriptorScope;
    }


    public String getDescriptorname() {
        return descriptorName;
    }

    public void setDescriptorname(String descriptorName) {
        this.descriptorName = descriptorName;
    }
    public String getDescriptorscope() {
        return descriptorScope;
    }

    public void setDescriptorscope(String descriptorScope) {
        this.descriptorScope = descriptorScope;
    }


}