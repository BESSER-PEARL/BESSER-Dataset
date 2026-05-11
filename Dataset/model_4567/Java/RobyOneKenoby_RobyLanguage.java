





import java.util.List;
import java.util.ArrayList;

public class RobyOneKenoby_RobyLanguage  {






    private List<RobyOneKenoby_LanguageElmt> robyonekenoby_languageelmts;


    public RobyOneKenoby_RobyLanguage(
    ) {
        this.robyonekenoby_languageelmts = new ArrayList<>();
    }

    public RobyOneKenoby_RobyLanguage(
        ArrayList<RobyOneKenoby_LanguageElmt> robyonekenoby_languageelmts    ) {
        this.robyonekenoby_languageelmts = robyonekenoby_languageelmts;
    }


    public List<RobyOneKenoby_LanguageElmt> getRobyonekenoby_languageelmts() {
        return robyonekenoby_languageelmts;
    }

    public void addRobyonekenoby_languageelmt(Robyonekenoby_languageelmt robyonekenoby_languageelmt) {
        this.robyonekenoby_languageelmts.add(robyonekenoby_languageelmt);
    }

}