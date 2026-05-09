





import java.util.List;
import java.util.ArrayList;

public class typeslibrary_TypeInstance extends Type {

    private int precision;
    private String literals;
    private int length;





    private typeslibrary_NativeType typeslibrary_nativetype;


    public typeslibrary_TypeInstance(
        int precision,        String literals,        int length    ) {
        super(
        );
        this.precision = precision;
        this.literals = literals;
        this.length = length;
    }


    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public String getLiterals() {
        return literals;
    }

    public void setLiterals(String literals) {
        this.literals = literals;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public typeslibrary_NativeType getTypeslibrary_nativetype() {
        return typeslibrary_nativetype;
    }

    public void setTypeslibrary_nativetype(typeslibrary_NativeType typeslibrary_nativetype) {
        this.typeslibrary_nativetype = typeslibrary_nativetype;
    }

}