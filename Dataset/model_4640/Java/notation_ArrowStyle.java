





import java.util.List;
import java.util.ArrayList;

public class notation_ArrowStyle extends Style {

    private String arrowTarget;
    private String arrowSource;



    public notation_ArrowStyle(
        String arrowTarget,        String arrowSource    ) {
        super(
        );
        this.arrowTarget = arrowTarget;
        this.arrowSource = arrowSource;
    }


    public String getArrowtarget() {
        return arrowTarget;
    }

    public void setArrowtarget(String arrowTarget) {
        this.arrowTarget = arrowTarget;
    }
    public String getArrowsource() {
        return arrowSource;
    }

    public void setArrowsource(String arrowSource) {
        this.arrowSource = arrowSource;
    }


}