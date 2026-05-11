





import java.util.List;
import java.util.ArrayList;

public class SPL_Event extends Session {

    private String eventId;





    private List<SPL_Declaration> spl_declarations;




    private List<SPL_Method> spl_methods;


    public SPL_Event(
        String eventId    ) {
        super(
        );
        this.eventId = eventId;
        this.spl_declarations = new ArrayList<>();
        this.spl_methods = new ArrayList<>();
    }

    public SPL_Event(
        String eventId        ArrayList<SPL_Declaration> spl_declarations,        ArrayList<SPL_Method> spl_methods    ) {
        this.eventId = eventId;
        this.spl_declarations = spl_declarations;
        this.spl_methods = spl_methods;
    }

    public String getEventid() {
        return eventId;
    }

    public void setEventid(String eventId) {
        this.eventId = eventId;
    }

    public List<SPL_Declaration> getSpl_declarations() {
        return spl_declarations;
    }

    public void addSpl_declaration(Spl_declaration spl_declaration) {
        this.spl_declarations.add(spl_declaration);
    }
    public List<SPL_Method> getSpl_methods() {
        return spl_methods;
    }

    public void addSpl_method(Spl_method spl_method) {
        this.spl_methods.add(spl_method);
    }

}