





import java.util.List;
import java.util.ArrayList;

public class jointPackage_BibTeX2DocBook_TrgPara  {

    private String content;





    private TrgSection trgsection;


    public jointPackage_BibTeX2DocBook_TrgPara(
        String content    ) {
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public TrgSection getTrgsection() {
        return trgsection;
    }

    public void setTrgsection(TrgSection trgsection) {
        this.trgsection = trgsection;
    }

}