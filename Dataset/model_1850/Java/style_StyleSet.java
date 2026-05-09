





import java.util.List;
import java.util.ArrayList;

public class style_StyleSet  {

    private String uid;
    private String name;





    private style_StyleLibrary style_stylelibrary;


    public style_StyleSet(
        String uid,        String name    ) {
        this.uid = uid;
        this.name = name;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public style_StyleLibrary getStyle_stylelibrary() {
        return style_stylelibrary;
    }

    public void setStyle_stylelibrary(style_StyleLibrary style_stylelibrary) {
        this.style_stylelibrary = style_stylelibrary;
    }

}