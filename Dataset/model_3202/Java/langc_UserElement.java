





import java.util.List;
import java.util.ArrayList;

public class langc_UserElement extends Element {

    private String kind;





    private langc_FileName langc_filename;




    private langc_ElementList langc_elementlist;


    public langc_UserElement(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public langc_FileName getLangc_filename() {
        return langc_filename;
    }

    public void setLangc_filename(langc_FileName langc_filename) {
        this.langc_filename = langc_filename;
    }
    public langc_ElementList getLangc_elementlist() {
        return langc_elementlist;
    }

    public void setLangc_elementlist(langc_ElementList langc_elementlist) {
        this.langc_elementlist = langc_elementlist;
    }

}