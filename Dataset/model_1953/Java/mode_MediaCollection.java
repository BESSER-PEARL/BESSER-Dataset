





import java.util.List;
import java.util.ArrayList;

public class mode_MediaCollection  {

    private String name;





    private mode_MediaLibrary mode_medialibrary;




    private mode_Device mode_device;




    private mode_User mode_user;




    private List<mode_Device> mode_devices;




    private mode_User mode_user;


    public mode_MediaCollection(
        String name    ) {
        this.name = name;
        this.mode_devices = new ArrayList<>();
    }

    public mode_MediaCollection(
        String name        ArrayList<mode_Device> mode_devices    ) {
        this.name = name;
        this.mode_devices = mode_devices;
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
    public mode_Device getMode_device() {
        return mode_device;
    }

    public void setMode_device(mode_Device mode_device) {
        this.mode_device = mode_device;
    }
    public mode_User getMode_user() {
        return mode_user;
    }

    public void setMode_user(mode_User mode_user) {
        this.mode_user = mode_user;
    }
    public List<mode_Device> getMode_devices() {
        return mode_devices;
    }

    public void addMode_device(Mode_device mode_device) {
        this.mode_devices.add(mode_device);
    }
    public mode_User getMode_user() {
        return mode_user;
    }

    public void setMode_user(mode_User mode_user) {
        this.mode_user = mode_user;
    }

}