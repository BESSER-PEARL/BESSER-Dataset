





import java.util.List;
import java.util.ArrayList;

public class commons_Timestamped  {

    private String modificationTime;
    private String creationTime;



    public commons_Timestamped(
        String modificationTime,        String creationTime    ) {
        this.modificationTime = modificationTime;
        this.creationTime = creationTime;
    }


    public String getModificationtime() {
        return modificationTime;
    }

    public void setModificationtime(String modificationTime) {
        this.modificationTime = modificationTime;
    }
    public String getCreationtime() {
        return creationTime;
    }

    public void setCreationtime(String creationTime) {
        this.creationTime = creationTime;
    }


}