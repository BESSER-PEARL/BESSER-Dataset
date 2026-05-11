





import java.util.List;
import java.util.ArrayList;

public class picojava_BooleanLiteral extends Exp {

    private String Value;





    private picojava_PrimitiveDecl picojava_primitivedecl;


    public picojava_BooleanLiteral(
        String Value    ) {
        super(
        );
        this.Value = Value;
    }


    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }

    public picojava_PrimitiveDecl getPicojava_primitivedecl() {
        return picojava_primitivedecl;
    }

    public void setPicojava_primitivedecl(picojava_PrimitiveDecl picojava_primitivedecl) {
        this.picojava_primitivedecl = picojava_primitivedecl;
    }

}