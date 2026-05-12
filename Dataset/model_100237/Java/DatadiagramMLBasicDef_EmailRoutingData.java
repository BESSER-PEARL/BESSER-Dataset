





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLBasicDef_EmailRoutingData  {

    private String size;
    private String data;





    private VisioDocument visiodocument;


    public DatadiagramMLBasicDef_EmailRoutingData(
        String size,        String data    ) {
        this.size = size;
        this.data = data;
    }


    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public VisioDocument getVisiodocument() {
        return visiodocument;
    }

    public void setVisiodocument(VisioDocument visiodocument) {
        this.visiodocument = visiodocument;
    }

}