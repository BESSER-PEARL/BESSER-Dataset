





import java.util.List;
import java.util.ArrayList;

public class ASM_AsmInvocation extends Rule {

    private String asmName;



    public ASM_AsmInvocation(
        String asmName    ) {
        super(
        );
        this.asmName = asmName;
    }


    public String getAsmname() {
        return asmName;
    }

    public void setAsmname(String asmName) {
        this.asmName = asmName;
    }


}