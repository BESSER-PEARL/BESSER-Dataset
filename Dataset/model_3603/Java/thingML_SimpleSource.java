





import java.util.List;
import java.util.ArrayList;

public class thingML_SimpleSource extends Source, ReferencedElmt {

    private String name;





    private thingML_ReceiveMessage thingml_receivemessage;


    public thingML_SimpleSource(
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

    public thingML_ReceiveMessage getThingml_receivemessage() {
        return thingml_receivemessage;
    }

    public void setThingml_receivemessage(thingML_ReceiveMessage thingml_receivemessage) {
        this.thingml_receivemessage = thingml_receivemessage;
    }

}