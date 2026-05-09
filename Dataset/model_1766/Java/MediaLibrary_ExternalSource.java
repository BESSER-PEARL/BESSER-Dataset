





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_ExternalSource extends MediaSource {

    private String sourceType;



    public MediaLibrary_ExternalSource(
        String sourceType    ) {
        super(
        );
        this.sourceType = sourceType;
    }


    public String getSourcetype() {
        return sourceType;
    }

    public void setSourcetype(String sourceType) {
        this.sourceType = sourceType;
    }


}