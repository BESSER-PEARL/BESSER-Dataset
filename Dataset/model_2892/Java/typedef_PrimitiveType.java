





import java.util.List;
import java.util.ArrayList;

public class typedef_PrimitiveType extends Type {

    private boolean nillable;
    private String typesetName;



    public typedef_PrimitiveType(
        boolean nillable,        String typesetName    ) {
        super(
        );
        this.nillable = nillable;
        this.typesetName = typesetName;
    }


    public boolean getNillable() {
        return nillable;
    }

    public void setNillable(boolean nillable) {
        this.nillable = nillable;
    }
    public String getTypesetname() {
        return typesetName;
    }

    public void setTypesetname(String typesetName) {
        this.typesetName = typesetName;
    }


}