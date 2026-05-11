





import java.util.List;
import java.util.ArrayList;

public class nuSMV_ConstantsDeclaration extends ModuleElement {

    private boolean semicolon;
    private String constants;



    public nuSMV_ConstantsDeclaration(
        boolean semicolon,        String constants    ) {
        super(
        );
        this.semicolon = semicolon;
        this.constants = constants;
    }


    public boolean getSemicolon() {
        return semicolon;
    }

    public void setSemicolon(boolean semicolon) {
        this.semicolon = semicolon;
    }
    public String getConstants() {
        return constants;
    }

    public void setConstants(String constants) {
        this.constants = constants;
    }


}