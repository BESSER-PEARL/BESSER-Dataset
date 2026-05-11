





import java.util.List;
import java.util.ArrayList;

public class notation_TitleStyle extends Style {

    private boolean showTitle;



    public notation_TitleStyle(
        boolean showTitle    ) {
        super(
        );
        this.showTitle = showTitle;
    }


    public boolean getShowtitle() {
        return showTitle;
    }

    public void setShowtitle(boolean showTitle) {
        this.showTitle = showTitle;
    }


}