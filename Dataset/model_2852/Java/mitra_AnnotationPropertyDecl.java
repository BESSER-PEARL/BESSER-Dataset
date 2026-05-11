





import java.util.List;
import java.util.ArrayList;

public class mitra_AnnotationPropertyDecl  {

    private String name;
    private boolean required;





    private mitra_AnnotationDecl mitra_annotationdecl;




    private mitra_PrimitiveType mitra_primitivetype;




    private mitra_Literal mitra_literal;


    public mitra_AnnotationPropertyDecl(
        String name,        boolean required    ) {
        this.name = name;
        this.required = required;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }

    public mitra_AnnotationDecl getMitra_annotationdecl() {
        return mitra_annotationdecl;
    }

    public void setMitra_annotationdecl(mitra_AnnotationDecl mitra_annotationdecl) {
        this.mitra_annotationdecl = mitra_annotationdecl;
    }
    public mitra_PrimitiveType getMitra_primitivetype() {
        return mitra_primitivetype;
    }

    public void setMitra_primitivetype(mitra_PrimitiveType mitra_primitivetype) {
        this.mitra_primitivetype = mitra_primitivetype;
    }
    public mitra_Literal getMitra_literal() {
        return mitra_literal;
    }

    public void setMitra_literal(mitra_Literal mitra_literal) {
        this.mitra_literal = mitra_literal;
    }

}