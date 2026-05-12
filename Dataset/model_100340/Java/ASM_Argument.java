





import java.util.List;
import java.util.ArrayList;

public class ASM_Argument extends VariableDecl {

    private String type;



    public ASM_Argument(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}