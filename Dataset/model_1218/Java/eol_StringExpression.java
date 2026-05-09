





import java.util.List;
import java.util.ArrayList;

public class eol_StringExpression extends SummableExpression, ComparableExpression {

    private String value;





    private eol_NativeType eol_nativetype;




    private eol_SimpleAnnotationStatement eol_simpleannotationstatement;


    public eol_StringExpression(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public eol_NativeType getEol_nativetype() {
        return eol_nativetype;
    }

    public void setEol_nativetype(eol_NativeType eol_nativetype) {
        this.eol_nativetype = eol_nativetype;
    }
    public eol_SimpleAnnotationStatement getEol_simpleannotationstatement() {
        return eol_simpleannotationstatement;
    }

    public void setEol_simpleannotationstatement(eol_SimpleAnnotationStatement eol_simpleannotationstatement) {
        this.eol_simpleannotationstatement = eol_simpleannotationstatement;
    }

}