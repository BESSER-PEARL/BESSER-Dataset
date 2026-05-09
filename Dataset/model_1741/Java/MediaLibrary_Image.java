





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_Image extends Artifact {

    private String dateTaken;



    public MediaLibrary_Image(
        String dateTaken    ) {
        super(
        );
        this.dateTaken = dateTaken;
    }


    public String getDatetaken() {
        return dateTaken;
    }

    public void setDatetaken(String dateTaken) {
        this.dateTaken = dateTaken;
    }


}