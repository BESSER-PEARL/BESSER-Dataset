





import java.util.List;
import java.util.ArrayList;

public class opf_Reference  {

    private String href;
    private String type;
    private String title;





    private opf_Guide opf_guide;


    public opf_Reference(
        String href,        String type,        String title    ) {
        this.href = href;
        this.type = type;
        this.title = title;
    }


    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public opf_Guide getOpf_guide() {
        return opf_guide;
    }

    public void setOpf_guide(opf_Guide opf_guide) {
        this.opf_guide = opf_guide;
    }

}