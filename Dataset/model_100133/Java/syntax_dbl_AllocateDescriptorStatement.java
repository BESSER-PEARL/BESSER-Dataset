





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_AllocateDescriptorStatement extends BindingStatement {

    private String withMax;
    private String descriptorScope;
    private String descriptorName;



    public syntax_dbl_AllocateDescriptorStatement(
        String withMax,        String descriptorScope,        String descriptorName    ) {
        super(
        );
        this.withMax = withMax;
        this.descriptorScope = descriptorScope;
        this.descriptorName = descriptorName;
    }


    public String getWithmax() {
        return withMax;
    }

    public void setWithmax(String withMax) {
        this.withMax = withMax;
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