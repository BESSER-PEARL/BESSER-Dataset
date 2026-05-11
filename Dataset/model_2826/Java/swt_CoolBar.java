





import java.util.List;
import java.util.ArrayList;

public class swt_CoolBar  {

    private String orientationStyle;





    private swt_CoolItem swt_coolitem;




    private List<swt_CoolItem> swt_coolitems;


    public swt_CoolBar(
        String orientationStyle    ) {
        this.orientationStyle = orientationStyle;
        this.swt_coolitems = new ArrayList<>();
    }

    public swt_CoolBar(
        String orientationStyle        ArrayList<swt_CoolItem> swt_coolitems    ) {
        this.orientationStyle = orientationStyle;
        this.swt_coolitems = swt_coolitems;
    }

    public String getOrientationstyle() {
        return orientationStyle;
    }

    public void setOrientationstyle(String orientationStyle) {
        this.orientationStyle = orientationStyle;
    }

    public swt_CoolItem getSwt_coolitem() {
        return swt_coolitem;
    }

    public void setSwt_coolitem(swt_CoolItem swt_coolitem) {
        this.swt_coolitem = swt_coolitem;
    }
    public List<swt_CoolItem> getSwt_coolitems() {
        return swt_coolitems;
    }

    public void addSwt_coolitem(Swt_coolitem swt_coolitem) {
        this.swt_coolitems.add(swt_coolitem);
    }

}