





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_File_a  {

    private String Onwer;
    private String size;
    private String ObjectURL;



    public PhotosMetaModel_File_a(
        String Onwer,        String size,        String ObjectURL    ) {
        this.Onwer = Onwer;
        this.size = size;
        this.ObjectURL = ObjectURL;
    }


    public String getOnwer() {
        return Onwer;
    }

    public void setOnwer(String Onwer) {
        this.Onwer = Onwer;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getObjecturl() {
        return ObjectURL;
    }

    public void setObjecturl(String ObjectURL) {
        this.ObjectURL = ObjectURL;
    }


}