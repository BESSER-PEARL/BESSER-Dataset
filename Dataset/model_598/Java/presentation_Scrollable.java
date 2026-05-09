





import java.util.List;
import java.util.ArrayList;

public class presentation_Scrollable extends Control {

    private String clientArea;
    private String group1;



    public presentation_Scrollable(
        String clientArea,        String group1    ) {
        super(
        );
        this.clientArea = clientArea;
        this.group1 = group1;
    }


    public String getClientarea() {
        return clientArea;
    }

    public void setClientarea(String clientArea) {
        this.clientArea = clientArea;
    }
    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }


}