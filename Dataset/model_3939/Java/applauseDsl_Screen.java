





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_Screen extends NamedElement {

    private String kind;
    private String title;



    public applauseDsl_Screen(
        String kind,        String title    ) {
        super(
        );
        this.kind = kind;
        this.title = title;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}