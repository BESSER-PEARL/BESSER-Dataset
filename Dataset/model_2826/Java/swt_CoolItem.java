





import java.util.List;
import java.util.ArrayList;

public class swt_CoolItem extends Item {

    private String minimumSize;
    private String size;
    private String preferredSize;





    private swt_Control swt_control;


    public swt_CoolItem(
        String minimumSize,        String size,        String preferredSize    ) {
        super(
        );
        this.minimumSize = minimumSize;
        this.size = size;
        this.preferredSize = preferredSize;
    }


    public String getMinimumsize() {
        return minimumSize;
    }

    public void setMinimumsize(String minimumSize) {
        this.minimumSize = minimumSize;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getPreferredsize() {
        return preferredSize;
    }

    public void setPreferredsize(String preferredSize) {
        this.preferredSize = preferredSize;
    }

    public swt_Control getSwt_control() {
        return swt_control;
    }

    public void setSwt_control(swt_Control swt_control) {
        this.swt_control = swt_control;
    }

}