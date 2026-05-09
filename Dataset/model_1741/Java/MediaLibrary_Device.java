





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_Device  {

    private int resolutionHeight;
    private int resolutionWidth;
    private String MACAddress;





    private MediaLibrary_Ecosystem medialibrary_ecosystem;


    public MediaLibrary_Device(
        int resolutionHeight,        int resolutionWidth,        String MACAddress    ) {
        this.resolutionHeight = resolutionHeight;
        this.resolutionWidth = resolutionWidth;
        this.MACAddress = MACAddress;
    }


    public int getResolutionheight() {
        return resolutionHeight;
    }

    public void setResolutionheight(int resolutionHeight) {
        this.resolutionHeight = resolutionHeight;
    }
    public int getResolutionwidth() {
        return resolutionWidth;
    }

    public void setResolutionwidth(int resolutionWidth) {
        this.resolutionWidth = resolutionWidth;
    }
    public String getMacaddress() {
        return MACAddress;
    }

    public void setMacaddress(String MACAddress) {
        this.MACAddress = MACAddress;
    }

    public MediaLibrary_Ecosystem getMedialibrary_ecosystem() {
        return medialibrary_ecosystem;
    }

    public void setMedialibrary_ecosystem(MediaLibrary_Ecosystem medialibrary_ecosystem) {
        this.medialibrary_ecosystem = medialibrary_ecosystem;
    }

}