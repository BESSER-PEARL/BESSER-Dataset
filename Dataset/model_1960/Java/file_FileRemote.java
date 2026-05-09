





import java.util.List;
import java.util.ArrayList;

public class file_FileRemote extends ByteFile {

    private String URL;



    public file_FileRemote(
        String URL    ) {
        super(
        );
        this.URL = URL;
    }


    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }


}