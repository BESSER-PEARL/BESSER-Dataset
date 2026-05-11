





import java.util.List;
import java.util.ArrayList;

public class web_Image  {

    private String label;
    private String src;





    private web_Gallery web_gallery;


    public web_Image(
        String label,        String src    ) {
        this.label = label;
        this.src = src;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }

    public web_Gallery getWeb_gallery() {
        return web_gallery;
    }

    public void setWeb_gallery(web_Gallery web_gallery) {
        this.web_gallery = web_gallery;
    }

}