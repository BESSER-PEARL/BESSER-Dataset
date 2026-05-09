





import java.util.List;
import java.util.ArrayList;

public class tda593_booking_Organization extends LegalEntity {

    private String name;
    private String organizationNumber;



    public tda593_booking_Organization(
        String name,        String organizationNumber    ) {
        super(
        );
        this.name = name;
        this.organizationNumber = organizationNumber;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOrganizationnumber() {
        return organizationNumber;
    }

    public void setOrganizationnumber(String organizationNumber) {
        this.organizationNumber = organizationNumber;
    }


}