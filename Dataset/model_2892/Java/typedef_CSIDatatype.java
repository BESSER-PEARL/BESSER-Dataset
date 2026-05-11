





import java.util.List;
import java.util.ArrayList;

public class typedef_CSIDatatype extends Type {

    private boolean nillable;
    private String code;



    public typedef_CSIDatatype(
        boolean nillable,        String code    ) {
        super(
        );
        this.nillable = nillable;
        this.code = code;
    }


    public boolean getNillable() {
        return nillable;
    }

    public void setNillable(boolean nillable) {
        this.nillable = nillable;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}