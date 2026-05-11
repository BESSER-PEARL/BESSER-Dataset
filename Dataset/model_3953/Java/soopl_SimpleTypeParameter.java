





import java.util.List;
import java.util.ArrayList;

public class soopl_SimpleTypeParameter extends Parameter {

    private String dataType;



    public soopl_SimpleTypeParameter(
        String dataType    ) {
        super(
        );
        this.dataType = dataType;
    }


    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }


}