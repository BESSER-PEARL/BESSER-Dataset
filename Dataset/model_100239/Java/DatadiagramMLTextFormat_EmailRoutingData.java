





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLTextFormat_EmailRoutingData  {

    private String data;
    private String size;





    private VisioDocument visiodocument;


    public DatadiagramMLTextFormat_EmailRoutingData(
        String data,        String size    ) {
        this.data = data;
        this.size = size;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public VisioDocument getVisiodocument() {
        return visiodocument;
    }

    public void setVisiodocument(VisioDocument visiodocument) {
        this.visiodocument = visiodocument;
    }

}