





import java.util.List;
import java.util.ArrayList;

public class libraryElement_Resource extends IVarElement, TypedConfigureableObject {

    private String y;
    private String x;
    private String deviceTypeResource;





    private libraryElement_Device libraryelement_device;




    private libraryElement_Device libraryelement_device;




    private libraryElement_FBNetwork libraryelement_fbnetwork;


    public libraryElement_Resource(
        String y,        String x,        String deviceTypeResource    ) {
        super(
        );
        this.y = y;
        this.x = x;
        this.deviceTypeResource = deviceTypeResource;
    }


    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getDevicetyperesource() {
        return deviceTypeResource;
    }

    public void setDevicetyperesource(String deviceTypeResource) {
        this.deviceTypeResource = deviceTypeResource;
    }

    public libraryElement_Device getLibraryelement_device() {
        return libraryelement_device;
    }

    public void setLibraryelement_device(libraryElement_Device libraryelement_device) {
        this.libraryelement_device = libraryelement_device;
    }
    public libraryElement_Device getLibraryelement_device() {
        return libraryelement_device;
    }

    public void setLibraryelement_device(libraryElement_Device libraryelement_device) {
        this.libraryelement_device = libraryelement_device;
    }
    public libraryElement_FBNetwork getLibraryelement_fbnetwork() {
        return libraryelement_fbnetwork;
    }

    public void setLibraryelement_fbnetwork(libraryElement_FBNetwork libraryelement_fbnetwork) {
        this.libraryelement_fbnetwork = libraryelement_fbnetwork;
    }

}