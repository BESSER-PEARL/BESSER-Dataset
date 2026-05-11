





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Collaboration extends RootElement {

    private String name;
    private boolean isClosed;



    public bpmn2_Collaboration(
        String name,        boolean isClosed    ) {
        super(
        );
        this.name = name;
        this.isClosed = isClosed;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }


}