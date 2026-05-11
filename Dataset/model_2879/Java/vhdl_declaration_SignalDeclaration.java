





import java.util.List;
import java.util.ArrayList;

public class vhdl_declaration_SignalDeclaration extends ValueDeclaration {

    private String kind;
    private String mode;



    public vhdl_declaration_SignalDeclaration(
        String kind,        String mode    ) {
        super(
        );
        this.kind = kind;
        this.mode = mode;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }


}