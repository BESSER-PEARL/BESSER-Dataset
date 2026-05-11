





import java.util.List;
import java.util.ArrayList;

public class soaml_Attachment  {

    private String mimeType;
    private String encoding;





    private soaml_Property soaml_property;


    public soaml_Attachment(
        String mimeType,        String encoding    ) {
        this.mimeType = mimeType;
        this.encoding = encoding;
    }


    public String getMimetype() {
        return mimeType;
    }

    public void setMimetype(String mimeType) {
        this.mimeType = mimeType;
    }
    public String getEncoding() {
        return encoding;
    }

    public void setEncoding(String encoding) {
        this.encoding = encoding;
    }

    public soaml_Property getSoaml_property() {
        return soaml_property;
    }

    public void setSoaml_property(soaml_Property soaml_property) {
        this.soaml_property = soaml_property;
    }

}