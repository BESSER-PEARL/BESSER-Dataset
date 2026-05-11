





import java.util.List;
import java.util.ArrayList;

public class lobj_Language  {

    private String code;
    private String language;





    private lobj_AbstractContent lobj_abstractcontent;


    public lobj_Language(
        String code,        String language    ) {
        this.code = code;
        this.language = language;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public lobj_AbstractContent getLobj_abstractcontent() {
        return lobj_abstractcontent;
    }

    public void setLobj_abstractcontent(lobj_AbstractContent lobj_abstractcontent) {
        this.lobj_abstractcontent = lobj_abstractcontent;
    }

}