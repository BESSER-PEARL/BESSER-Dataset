





import java.util.List;
import java.util.ArrayList;

public class Author  {






    private BIBTEXML_Booklet bibtexml_booklet;




    private BIBTEXML_Misc bibtexml_misc;




    private BIBTEXML_AuthoredEntry bibtexml_authoredentry;


    public Author(
    ) {
    }



    public BIBTEXML_Booklet getBibtexml_booklet() {
        return bibtexml_booklet;
    }

    public void setBibtexml_booklet(BIBTEXML_Booklet bibtexml_booklet) {
        this.bibtexml_booklet = bibtexml_booklet;
    }
    public BIBTEXML_Misc getBibtexml_misc() {
        return bibtexml_misc;
    }

    public void setBibtexml_misc(BIBTEXML_Misc bibtexml_misc) {
        this.bibtexml_misc = bibtexml_misc;
    }
    public BIBTEXML_AuthoredEntry getBibtexml_authoredentry() {
        return bibtexml_authoredentry;
    }

    public void setBibtexml_authoredentry(BIBTEXML_AuthoredEntry bibtexml_authoredentry) {
        this.bibtexml_authoredentry = bibtexml_authoredentry;
    }

}