





import java.util.List;
import java.util.ArrayList;

public class libraryElement_SystemConfiguration extends I4DIACElement {






    private List<libraryElement_Segment> libraryelement_segments;




    private List<libraryElement_Link> libraryelement_links;




    private List<libraryElement_Device> libraryelement_devices;




    private libraryElement_AutomationSystem libraryelement_automationsystem;


    public libraryElement_SystemConfiguration(
    ) {
        super(
        );
        this.libraryelement_segments = new ArrayList<>();
        this.libraryelement_links = new ArrayList<>();
        this.libraryelement_devices = new ArrayList<>();
    }

    public libraryElement_SystemConfiguration(
        ArrayList<libraryElement_Segment> libraryelement_segments,        ArrayList<libraryElement_Link> libraryelement_links,        ArrayList<libraryElement_Device> libraryelement_devices    ) {
        this.libraryelement_segments = libraryelement_segments;
        this.libraryelement_links = libraryelement_links;
        this.libraryelement_devices = libraryelement_devices;
    }


    public List<libraryElement_Segment> getLibraryelement_segments() {
        return libraryelement_segments;
    }

    public void addLibraryelement_segment(Libraryelement_segment libraryelement_segment) {
        this.libraryelement_segments.add(libraryelement_segment);
    }
    public List<libraryElement_Link> getLibraryelement_links() {
        return libraryelement_links;
    }

    public void addLibraryelement_link(Libraryelement_link libraryelement_link) {
        this.libraryelement_links.add(libraryelement_link);
    }
    public List<libraryElement_Device> getLibraryelement_devices() {
        return libraryelement_devices;
    }

    public void addLibraryelement_device(Libraryelement_device libraryelement_device) {
        this.libraryelement_devices.add(libraryelement_device);
    }
    public libraryElement_AutomationSystem getLibraryelement_automationsystem() {
        return libraryelement_automationsystem;
    }

    public void setLibraryelement_automationsystem(libraryElement_AutomationSystem libraryelement_automationsystem) {
        this.libraryelement_automationsystem = libraryelement_automationsystem;
    }

}