





import java.util.List;
import java.util.ArrayList;

public class vhdl_declaration_FunctionDeclaration extends declaration_SubprogramDeclaration, type_Typed {

    private String purity;



    public vhdl_declaration_FunctionDeclaration(
        String purity    ) {
        super(
        );
        this.purity = purity;
    }


    public String getPurity() {
        return purity;
    }

    public void setPurity(String purity) {
        this.purity = purity;
    }


}