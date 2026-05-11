





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_TrgEvent extends TrgSession {

    private String eventId;





    private List<TrgDeclaration> trgdeclarations;


    public jointPackage_CPL2SPL_TrgEvent(
        String eventId    ) {
        super(
        );
        this.eventId = eventId;
        this.trgdeclarations = new ArrayList<>();
    }

    public jointPackage_CPL2SPL_TrgEvent(
        String eventId        ArrayList<TrgDeclaration> trgdeclarations    ) {
        this.eventId = eventId;
        this.trgdeclarations = trgdeclarations;
    }

    public String getEventid() {
        return eventId;
    }

    public void setEventid(String eventId) {
        this.eventId = eventId;
    }

    public List<TrgDeclaration> getTrgdeclarations() {
        return trgdeclarations;
    }

    public void addTrgdeclaration(Trgdeclaration trgdeclaration) {
        this.trgdeclarations.add(trgdeclaration);
    }

}