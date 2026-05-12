





import java.util.List;
import java.util.ArrayList;

public class bibtex_School  {

    private String school;





    private bibtex_Mastersthesis bibtex_mastersthesis;


    public bibtex_School(
        String school    ) {
        this.school = school;
    }


    public String getSchool() {
        return school;
    }

    public void setSchool(String school) {
        this.school = school;
    }

    public bibtex_Mastersthesis getBibtex_mastersthesis() {
        return bibtex_mastersthesis;
    }

    public void setBibtex_mastersthesis(bibtex_Mastersthesis bibtex_mastersthesis) {
        this.bibtex_mastersthesis = bibtex_mastersthesis;
    }

}