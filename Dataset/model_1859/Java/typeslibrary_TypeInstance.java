





import java.util.List;
import java.util.ArrayList;

public class typeslibrary_TypeInstance extends Type {

    private int precision;
    private int length;
    private String literals;





    private typeslibrary_SimpleNamedType typeslibrary_simplenamedtype;




    private typeslibrary_NativeType typeslibrary_nativetype;


    public typeslibrary_TypeInstance(
        int precision,        int length,        String literals    ) {
        super(
        );
        this.precision = precision;
        this.length = length;
        this.literals = literals;
    }


    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getLiterals() {
        return literals;
    }

    public void setLiterals(String literals) {
        this.literals = literals;
    }

    public typeslibrary_SimpleNamedType getTypeslibrary_simplenamedtype() {
        return typeslibrary_simplenamedtype;
    }

    public void setTypeslibrary_simplenamedtype(typeslibrary_SimpleNamedType typeslibrary_simplenamedtype) {
        this.typeslibrary_simplenamedtype = typeslibrary_simplenamedtype;
    }
    public typeslibrary_NativeType getTypeslibrary_nativetype() {
        return typeslibrary_nativetype;
    }

    public void setTypeslibrary_nativetype(typeslibrary_NativeType typeslibrary_nativetype) {
        this.typeslibrary_nativetype = typeslibrary_nativetype;
    }

}