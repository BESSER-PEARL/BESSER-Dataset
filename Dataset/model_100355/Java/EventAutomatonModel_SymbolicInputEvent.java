





import java.util.List;
import java.util.ArrayList;

public class EventAutomatonModel_SymbolicInputEvent extends SymbolicEvent {

    private String name;



    public EventAutomatonModel_SymbolicInputEvent(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}