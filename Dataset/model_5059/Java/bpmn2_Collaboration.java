





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Collaboration extends RootElement {

    private boolean isClosed;
    private String name;



    public bpmn2_Collaboration(
        boolean isClosed,        String name    ) {
        super(
        );
        this.isClosed = isClosed;
        this.name = name;
    }


    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}