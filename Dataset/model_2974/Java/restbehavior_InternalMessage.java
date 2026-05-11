





import java.util.List;
import java.util.ArrayList;

public class restbehavior_InternalMessage extends Trigger {

    private String name;



    public restbehavior_InternalMessage(
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