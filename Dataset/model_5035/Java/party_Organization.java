





import java.util.List;
import java.util.ArrayList;

public class party_Organization extends Party {

    private String organizationType;



    public party_Organization(
        String organizationType    ) {
        super(
        );
        this.organizationType = organizationType;
    }


    public String getOrganizationtype() {
        return organizationType;
    }

    public void setOrganizationtype(String organizationType) {
        this.organizationType = organizationType;
    }


}