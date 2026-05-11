





import java.util.List;
import java.util.ArrayList;

public class notation_View extends NotationElement {

    private String viewDetails;
    private String viewType;



    public notation_View(
        String viewDetails,        String viewType    ) {
        super(
        );
        this.viewDetails = viewDetails;
        this.viewType = viewType;
    }


    public String getViewdetails() {
        return viewDetails;
    }

    public void setViewdetails(String viewDetails) {
        this.viewDetails = viewDetails;
    }
    public String getViewtype() {
        return viewType;
    }

    public void setViewtype(String viewType) {
        this.viewType = viewType;
    }


}