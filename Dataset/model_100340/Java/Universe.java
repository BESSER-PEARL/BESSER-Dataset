





import java.util.List;
import java.util.ArrayList;

public class Universe  {






    private ASM_Universe asm_universe;




    private ASM_DoForallRule asm_doforallrule;




    private ASM_ChooseRule asm_chooserule;




    private ASM_Extension asm_extension;


    public Universe(
    ) {
    }



    public ASM_Universe getAsm_universe() {
        return asm_universe;
    }

    public void setAsm_universe(ASM_Universe asm_universe) {
        this.asm_universe = asm_universe;
    }
    public ASM_DoForallRule getAsm_doforallrule() {
        return asm_doforallrule;
    }

    public void setAsm_doforallrule(ASM_DoForallRule asm_doforallrule) {
        this.asm_doforallrule = asm_doforallrule;
    }
    public ASM_ChooseRule getAsm_chooserule() {
        return asm_chooserule;
    }

    public void setAsm_chooserule(ASM_ChooseRule asm_chooserule) {
        this.asm_chooserule = asm_chooserule;
    }
    public ASM_Extension getAsm_extension() {
        return asm_extension;
    }

    public void setAsm_extension(ASM_Extension asm_extension) {
        this.asm_extension = asm_extension;
    }

}