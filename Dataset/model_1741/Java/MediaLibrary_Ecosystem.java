





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_Ecosystem  {






    private List<MediaLibrary_Library> medialibrary_librarys;


    public MediaLibrary_Ecosystem(
    ) {
        this.medialibrary_librarys = new ArrayList<>();
    }

    public MediaLibrary_Ecosystem(
        ArrayList<MediaLibrary_Library> medialibrary_librarys    ) {
        this.medialibrary_librarys = medialibrary_librarys;
    }


    public List<MediaLibrary_Library> getMedialibrary_librarys() {
        return medialibrary_librarys;
    }

    public void addMedialibrary_library(Medialibrary_library medialibrary_library) {
        this.medialibrary_librarys.add(medialibrary_library);
    }

}