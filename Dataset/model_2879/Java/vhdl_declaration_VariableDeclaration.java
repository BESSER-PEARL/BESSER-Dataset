





import java.util.List;
import java.util.ArrayList;

public class vhdl_declaration_VariableDeclaration extends ValueDeclaration {

    private boolean shared;
    private String mode;



    public vhdl_declaration_VariableDeclaration(
        boolean shared,        String mode    ) {
        super(
        );
        this.shared = shared;
        this.mode = mode;
    }


    public boolean getShared() {
        return shared;
    }

    public void setShared(boolean shared) {
        this.shared = shared;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }


}