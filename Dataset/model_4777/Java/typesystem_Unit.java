





import java.util.List;
import java.util.ArrayList;

public class typesystem_Unit  {

    private boolean wildcard;
    private int scale;





    private typesystem_NumericType typesystem_numerictype;


    public typesystem_Unit(
        boolean wildcard,        int scale    ) {
        this.wildcard = wildcard;
        this.scale = scale;
    }


    public boolean getWildcard() {
        return wildcard;
    }

    public void setWildcard(boolean wildcard) {
        this.wildcard = wildcard;
    }
    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }

    public typesystem_NumericType getTypesystem_numerictype() {
        return typesystem_numerictype;
    }

    public void setTypesystem_numerictype(typesystem_NumericType typesystem_numerictype) {
        this.typesystem_numerictype = typesystem_numerictype;
    }

}