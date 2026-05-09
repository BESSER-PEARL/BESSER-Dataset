





import java.util.List;
import java.util.ArrayList;

public class addressbook_Organization extends NamedElement, Entry {

    private String homepage;



    public addressbook_Organization(
        String homepage    ) {
        super(
        );
        this.homepage = homepage;
    }


    public String getHomepage() {
        return homepage;
    }

    public void setHomepage(String homepage) {
        this.homepage = homepage;
    }


}