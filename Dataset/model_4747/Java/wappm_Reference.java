





import java.util.List;
import java.util.ArrayList;

public class wappm_Reference  {

    private int upBound;
    private int lowBound;
    private String name;





    private wappm_WebClass wappm_webclass;


    public wappm_Reference(
        int upBound,        int lowBound,        String name    ) {
        this.upBound = upBound;
        this.lowBound = lowBound;
        this.name = name;
    }


    public int getUpbound() {
        return upBound;
    }

    public void setUpbound(int upBound) {
        this.upBound = upBound;
    }
    public int getLowbound() {
        return lowBound;
    }

    public void setLowbound(int lowBound) {
        this.lowBound = lowBound;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public wappm_WebClass getWappm_webclass() {
        return wappm_webclass;
    }

    public void setWappm_webclass(wappm_WebClass wappm_webclass) {
        this.wappm_webclass = wappm_webclass;
    }

}