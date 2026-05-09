





import java.util.List;
import java.util.ArrayList;

public class mpupkb_Comment  {

    private String content;





    private mpupkb_NamedElement mpupkb_namedelement;


    public mpupkb_Comment(
        String content    ) {
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public mpupkb_NamedElement getMpupkb_namedelement() {
        return mpupkb_namedelement;
    }

    public void setMpupkb_namedelement(mpupkb_NamedElement mpupkb_namedelement) {
        this.mpupkb_namedelement = mpupkb_namedelement;
    }

}