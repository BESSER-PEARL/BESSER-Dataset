





import java.util.List;
import java.util.ArrayList;

public class sooml_Parameter extends NamedElement {

    private String dataType;





    private sooml_Class sooml_class;


    public sooml_Parameter(
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

    public sooml_Class getSooml_class() {
        return sooml_class;
    }

    public void setSooml_class(sooml_Class sooml_class) {
        this.sooml_class = sooml_class;
    }

}