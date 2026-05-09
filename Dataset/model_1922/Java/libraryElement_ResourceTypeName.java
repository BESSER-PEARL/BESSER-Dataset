





import java.util.List;
import java.util.ArrayList;

public class libraryElement_ResourceTypeName  {

    private String name;





    private libraryElement_DeviceType libraryelement_devicetype;


    public libraryElement_ResourceTypeName(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public libraryElement_DeviceType getLibraryelement_devicetype() {
        return libraryelement_devicetype;
    }

    public void setLibraryelement_devicetype(libraryElement_DeviceType libraryelement_devicetype) {
        this.libraryelement_devicetype = libraryelement_devicetype;
    }

}