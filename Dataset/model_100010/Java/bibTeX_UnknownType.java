





import java.util.List;
import java.util.ArrayList;

public class bibTeX_UnknownType  {

    private String type;





    private bibTeX_UnknownField bibtex_unknownfield;


    public bibTeX_UnknownType(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public bibTeX_UnknownField getBibtex_unknownfield() {
        return bibtex_unknownfield;
    }

    public void setBibtex_unknownfield(bibTeX_UnknownField bibtex_unknownfield) {
        this.bibtex_unknownfield = bibtex_unknownfield;
    }

}