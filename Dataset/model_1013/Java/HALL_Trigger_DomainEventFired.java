





import java.util.List;
import java.util.ArrayList;

public class HALL_Trigger_DomainEventFired extends TriggerExpression {

    private String name;



    public HALL_Trigger_DomainEventFired(
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