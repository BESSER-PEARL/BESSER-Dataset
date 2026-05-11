





import java.util.List;
import java.util.ArrayList;

public class frameweb_FrameworkProfile extends Profile {

    private String category;
    private String kind;





    private frameweb_FramewebProject frameweb_framewebproject;


    public frameweb_FrameworkProfile(
        String category,        String kind    ) {
        super(
        );
        this.category = category;
        this.kind = kind;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public frameweb_FramewebProject getFrameweb_framewebproject() {
        return frameweb_framewebproject;
    }

    public void setFrameweb_framewebproject(frameweb_FramewebProject frameweb_framewebproject) {
        this.frameweb_framewebproject = frameweb_framewebproject;
    }

}