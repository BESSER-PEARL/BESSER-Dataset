





import java.util.List;
import java.util.ArrayList;

public class ASM_Function extends ElementDecl, Declaration {

    private String returnType;
    private String isExternal;



    public ASM_Function(
        String returnType,        String isExternal    ) {
        super(
        );
        this.returnType = returnType;
        this.isExternal = isExternal;
    }


    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }
    public String getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(String isExternal) {
        this.isExternal = isExternal;
    }


}