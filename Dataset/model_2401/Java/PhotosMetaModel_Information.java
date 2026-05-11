





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Information extends Modules {

    private String fileType;



    public PhotosMetaModel_Information(
        String fileType    ) {
        super(
        );
        this.fileType = fileType;
    }


    public String getFiletype() {
        return fileType;
    }

    public void setFiletype(String fileType) {
        this.fileType = fileType;
    }


}