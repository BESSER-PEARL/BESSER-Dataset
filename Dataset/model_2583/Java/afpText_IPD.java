





import java.util.List;
import java.util.ArrayList;

public class afpText_IPD extends structuredField {

    private String IOCAdat;
    private String imageData;



    public afpText_IPD(
        String IOCAdat,        String imageData    ) {
        super(
        );
        this.IOCAdat = IOCAdat;
        this.imageData = imageData;
    }


    public String getIocadat() {
        return IOCAdat;
    }

    public void setIocadat(String IOCAdat) {
        this.IOCAdat = IOCAdat;
    }
    public String getImagedata() {
        return imageData;
    }

    public void setImagedata(String imageData) {
        this.imageData = imageData;
    }


}