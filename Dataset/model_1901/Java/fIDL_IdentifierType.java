





import java.util.List;
import java.util.ArrayList;

public class fIDL_IdentifierType extends Type {

    private boolean nullable;





    private fIDL_Declaration fidl_declaration;


    public fIDL_IdentifierType(
        boolean nullable    ) {
        super(
        );
        this.nullable = nullable;
    }


    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }

    public fIDL_Declaration getFidl_declaration() {
        return fidl_declaration;
    }

    public void setFidl_declaration(fIDL_Declaration fidl_declaration) {
        this.fidl_declaration = fidl_declaration;
    }

}