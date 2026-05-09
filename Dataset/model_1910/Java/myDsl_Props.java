





import java.util.List;
import java.util.ArrayList;

public class myDsl_Props  {

    private String name;
    private String componentclass;



    public myDsl_Props(
        String name,        String componentclass    ) {
        this.name = name;
        this.componentclass = componentclass;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComponentclass() {
        return componentclass;
    }

    public void setComponentclass(String componentclass) {
        this.componentclass = componentclass;
    }


}