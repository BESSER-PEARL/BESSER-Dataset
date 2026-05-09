





import java.util.List;
import java.util.ArrayList;

public class mode_Device  {

    private String type;
    private String name;





    private mode_MediaLibrary mode_medialibrary;


    public mode_Device(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mode_MediaLibrary getMode_medialibrary() {
        return mode_medialibrary;
    }

    public void setMode_medialibrary(mode_MediaLibrary mode_medialibrary) {
        this.mode_medialibrary = mode_medialibrary;
    }

}