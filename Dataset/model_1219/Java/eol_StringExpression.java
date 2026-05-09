





import java.util.List;
import java.util.ArrayList;

public class eol_StringExpression extends PrimitiveExpression {

    private String val;





    private eol_NativeType eol_nativetype;




    private eol_Import eol_import;




    private eol_NativeExpression eol_nativeexpression;


    public eol_StringExpression(
        String val    ) {
        super(
        );
        this.val = val;
    }


    public String getVal() {
        return val;
    }

    public void setVal(String val) {
        this.val = val;
    }

    public eol_NativeType getEol_nativetype() {
        return eol_nativetype;
    }

    public void setEol_nativetype(eol_NativeType eol_nativetype) {
        this.eol_nativetype = eol_nativetype;
    }
    public eol_Import getEol_import() {
        return eol_import;
    }

    public void setEol_import(eol_Import eol_import) {
        this.eol_import = eol_import;
    }
    public eol_NativeExpression getEol_nativeexpression() {
        return eol_nativeexpression;
    }

    public void setEol_nativeexpression(eol_NativeExpression eol_nativeexpression) {
        this.eol_nativeexpression = eol_nativeexpression;
    }

}