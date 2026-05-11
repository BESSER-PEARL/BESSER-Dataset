





import java.util.List;
import java.util.ArrayList;

public class services_ServiceInterrest  {

    private String interrestKind;
    private String contactUnit;



    public services_ServiceInterrest(
        String interrestKind,        String contactUnit    ) {
        this.interrestKind = interrestKind;
        this.contactUnit = contactUnit;
    }


    public String getInterrestkind() {
        return interrestKind;
    }

    public void setInterrestkind(String interrestKind) {
        this.interrestKind = interrestKind;
    }
    public String getContactunit() {
        return contactUnit;
    }

    public void setContactunit(String contactUnit) {
        this.contactUnit = contactUnit;
    }


}