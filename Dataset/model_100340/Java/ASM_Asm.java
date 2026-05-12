





import java.util.List;
import java.util.ArrayList;

public class ASM_Asm extends LocatedElement {

    private String returnType;



    public ASM_Asm(
        String returnType    ) {
        super(
        );
        this.returnType = returnType;
    }


    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }


}