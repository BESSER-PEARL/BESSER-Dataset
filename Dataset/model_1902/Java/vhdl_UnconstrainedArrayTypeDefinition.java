





import java.util.List;
import java.util.ArrayList;

public class vhdl_UnconstrainedArrayTypeDefinition extends ArrayTypeDefinition {

    private String index;



    public vhdl_UnconstrainedArrayTypeDefinition(
        String index    ) {
        super(
        );
        this.index = index;
    }


    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }


}