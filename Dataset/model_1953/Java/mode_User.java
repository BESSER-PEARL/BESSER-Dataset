





import java.util.List;
import java.util.ArrayList;

public class mode_User  {

    private String name;





    private mode_MediaLibrary mode_medialibrary;


    public mode_User(
        String name    ) {
        this.name = name;
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