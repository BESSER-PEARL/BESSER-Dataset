





import java.util.List;
import java.util.ArrayList;

public class form_Label extends Element {

    private String for_;
    private String content;



    public form_Label(
        String for_,        String content    ) {
        super(
        );
        this.for_ = for_;
        this.content = content;
    }


    public String getFor_() {
        return for_;
    }

    public void setFor_(String for_) {
        this.for_ = for_;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}