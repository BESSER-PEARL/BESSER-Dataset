





import java.util.List;
import java.util.ArrayList;

public class langc_DependencyBlob extends Dependency {

    private String markerComment;
    private String text;



    public langc_DependencyBlob(
        String markerComment,        String text    ) {
        super(
        );
        this.markerComment = markerComment;
        this.text = text;
    }


    public String getMarkercomment() {
        return markerComment;
    }

    public void setMarkercomment(String markerComment) {
        this.markerComment = markerComment;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}