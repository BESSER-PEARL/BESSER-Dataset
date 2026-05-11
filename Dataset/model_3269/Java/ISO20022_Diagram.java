





import java.util.List;
import java.util.ArrayList;

public class ISO20022_Diagram extends RepositoryConcept {

    private String location;
    private String content;





    private ISO20022_Repository iso20022_repository;




    private ISO20022_Repository iso20022_repository;


    public ISO20022_Diagram(
        String location,        String content    ) {
        super(
        );
        this.location = location;
        this.content = content;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public ISO20022_Repository getIso20022_repository() {
        return iso20022_repository;
    }

    public void setIso20022_repository(ISO20022_Repository iso20022_repository) {
        this.iso20022_repository = iso20022_repository;
    }
    public ISO20022_Repository getIso20022_repository() {
        return iso20022_repository;
    }

    public void setIso20022_repository(ISO20022_Repository iso20022_repository) {
        this.iso20022_repository = iso20022_repository;
    }

}