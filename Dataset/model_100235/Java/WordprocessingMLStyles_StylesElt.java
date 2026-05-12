





import java.util.List;
import java.util.ArrayList;

public class WordprocessingMLStyles_StylesElt  {

    private None versionOfBuiltInStylenames;





    private List<StyleElt> styleelts;




    private WordDocument worddocument;


    public WordprocessingMLStyles_StylesElt(
        None versionOfBuiltInStylenames    ) {
        this.versionOfBuiltInStylenames = versionOfBuiltInStylenames;
        this.styleelts = new ArrayList<>();
    }

    public WordprocessingMLStyles_StylesElt(
        None versionOfBuiltInStylenames        ArrayList<StyleElt> styleelts    ) {
        this.versionOfBuiltInStylenames = versionOfBuiltInStylenames;
        this.styleelts = styleelts;
    }

    public None getVersionofbuiltinstylenames() {
        return versionOfBuiltInStylenames;
    }

    public void setVersionofbuiltinstylenames(None versionOfBuiltInStylenames) {
        this.versionOfBuiltInStylenames = versionOfBuiltInStylenames;
    }

    public List<StyleElt> getStyleelts() {
        return styleelts;
    }

    public void addStyleelt(Styleelt styleelt) {
        this.styleelts.add(styleelt);
    }
    public WordDocument getWorddocument() {
        return worddocument;
    }

    public void setWorddocument(WordDocument worddocument) {
        this.worddocument = worddocument;
    }

}