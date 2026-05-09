





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_MediaCollection  {

    private String name;





    private List<MediaLibrary_Artifact> medialibrary_artifacts;




    private MediaLibrary_Device medialibrary_device;




    private MediaLibrary_Device medialibrary_device;




    private List<MediaLibrary_Device> medialibrary_devices;




    private MediaLibrary_Library medialibrary_library;




    private MediaLibrary_Device medialibrary_device;


    public MediaLibrary_MediaCollection(
        String name    ) {
        this.name = name;
        this.medialibrary_artifacts = new ArrayList<>();
        this.medialibrary_devices = new ArrayList<>();
    }

    public MediaLibrary_MediaCollection(
        String name        ArrayList<MediaLibrary_Artifact> medialibrary_artifacts,        ArrayList<MediaLibrary_Device> medialibrary_devices    ) {
        this.name = name;
        this.medialibrary_artifacts = medialibrary_artifacts;
        this.medialibrary_devices = medialibrary_devices;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<MediaLibrary_Artifact> getMedialibrary_artifacts() {
        return medialibrary_artifacts;
    }

    public void addMedialibrary_artifact(Medialibrary_artifact medialibrary_artifact) {
        this.medialibrary_artifacts.add(medialibrary_artifact);
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
    public List<MediaLibrary_Device> getMedialibrary_devices() {
        return medialibrary_devices;
    }

    public void addMedialibrary_device(Medialibrary_device medialibrary_device) {
        this.medialibrary_devices.add(medialibrary_device);
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

}