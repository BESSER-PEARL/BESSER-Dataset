





import java.util.List;
import java.util.ArrayList;

public class diastyle_DStyleBridge  {

    private String name;





    private diastyle_DBaseStyle diastyle_dbasestyle;


    public diastyle_DStyleBridge(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public diastyle_DBaseStyle getDiastyle_dbasestyle() {
        return diastyle_dbasestyle;
    }

    public void setDiastyle_dbasestyle(diastyle_DBaseStyle diastyle_dbasestyle) {
        this.diastyle_dbasestyle = diastyle_dbasestyle;
    }

}