





import java.util.List;
import java.util.ArrayList;

public class contentfwk_OrganizationUnit extends Element {

    private String headcount;





    private contentfwk_Driver contentfwk_driver;




    private List<contentfwk_Driver> contentfwk_drivers;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;


    public contentfwk_OrganizationUnit(
        String headcount    ) {
        super(
        );
        this.headcount = headcount;
        this.contentfwk_drivers = new ArrayList<>();
    }

    public contentfwk_OrganizationUnit(
        String headcount        ArrayList<contentfwk_Driver> contentfwk_drivers    ) {
        this.headcount = headcount;
        this.contentfwk_drivers = contentfwk_drivers;
    }

    public String getHeadcount() {
        return headcount;
    }

    public void setHeadcount(String headcount) {
        this.headcount = headcount;
    }

    public contentfwk_Driver getContentfwk_driver() {
        return contentfwk_driver;
    }

    public void setContentfwk_driver(contentfwk_Driver contentfwk_driver) {
        this.contentfwk_driver = contentfwk_driver;
    }
    public List<contentfwk_Driver> getContentfwk_drivers() {
        return contentfwk_drivers;
    }

    public void addContentfwk_driver(Contentfwk_driver contentfwk_driver) {
        this.contentfwk_drivers.add(contentfwk_driver);
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }

}