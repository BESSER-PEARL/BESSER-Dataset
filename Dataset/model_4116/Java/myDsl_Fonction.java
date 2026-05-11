





import java.util.List;
import java.util.ArrayList;

public class myDsl_Fonction  {

    private String symbole;





    private myDsl_Programme mydsl_programme;


    public myDsl_Fonction(
        String symbole    ) {
        this.symbole = symbole;
    }


    public String getSymbole() {
        return symbole;
    }

    public void setSymbole(String symbole) {
        this.symbole = symbole;
    }

    public myDsl_Programme getMydsl_programme() {
        return mydsl_programme;
    }

    public void setMydsl_programme(myDsl_Programme mydsl_programme) {
        this.mydsl_programme = mydsl_programme;
    }

}