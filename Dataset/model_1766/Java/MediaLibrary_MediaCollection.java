





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_MediaCollection extends NamedElement {






    private MediaLibrary_Device medialibrary_device;




    private MediaLibrary_Device medialibrary_device;




    private MediaLibrary_Library medialibrary_library;




    private MediaLibrary_Device medialibrary_device;




    private List<MediaLibrary_Device> medialibrary_devices;


    public MediaLibrary_MediaCollection(
    ) {
        super(
        );
        this.medialibrary_devices = new ArrayList<>();
    }

    public MediaLibrary_MediaCollection(
        ArrayList<MediaLibrary_Device> medialibrary_devices    ) {
        this.medialibrary_devices = medialibrary_devices;
    }


    public MediaLibrary_Device getMedialibrary_device() {
        return medialibrary_device;
    }

    public void setMedialibrary_device(MediaLibrary_Device medialibrary_device) {
        this.medialibrary_device = medialibrary_device;
    }
    public MediaLibrary_Device getMedialibrary_device() {
        return medialibrary_device;
    }

    public void setMedialibrary_device(MediaLibrary_Device medialibrary_device) {
        this.medialibrary_device = medialibrary_device;
    }
    public MediaLibrary_Library getMedialibrary_library() {
        return medialibrary_library;
    }

    public void setMedialibrary_library(MediaLibrary_Library medialibrary_library) {
        this.medialibrary_library = medialibrary_library;
    }
    public MediaLibrary_Device getMedialibrary_device() {
        return medialibrary_device;
    }

    public void setMedialibrary_device(MediaLibrary_Device medialibrary_device) {
        this.medialibrary_device = medialibrary_device;
    }
    public List<MediaLibrary_Device> getMedialibrary_devices() {
        return medialibrary_devices;
    }

    public void addMedialibrary_device(Medialibrary_device medialibrary_device) {
        this.medialibrary_devices.add(medialibrary_device);
    }

}