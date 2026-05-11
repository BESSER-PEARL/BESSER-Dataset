





import java.util.List;
import java.util.ArrayList;

public class soaml_MessageType  {

    private String encoding;





    private soaml_Class soaml_class;


    public soaml_MessageType(
        String encoding    ) {
        this.encoding = encoding;
    }


    public String getEncoding() {
        return encoding;
    }

    public void setEncoding(String encoding) {
        this.encoding = encoding;
    }

    public soaml_Class getSoaml_class() {
        return soaml_class;
    }

    public void setSoaml_class(soaml_Class soaml_class) {
        this.soaml_class = soaml_class;
    }

}