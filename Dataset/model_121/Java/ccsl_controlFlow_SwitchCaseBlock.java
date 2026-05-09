





import java.util.List;
import java.util.ArrayList;

public class ccsl_controlFlow_SwitchCaseBlock extends Block {

    private String default;



    public ccsl_controlFlow_SwitchCaseBlock(
        String default    ) {
        super(
        );
        this.default = default;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }


}