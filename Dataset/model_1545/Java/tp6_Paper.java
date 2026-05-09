





import java.util.List;
import java.util.ArrayList;

public class tp6_Paper  {

    private String name;





    private tp6_PublicationStructure tp6_publicationstructure;




    private List<tp6_Researcher> tp6_researchers;




    private tp6_Paper tp6_paper;




    private List<tp6_PaperKeywords> tp6_paperkeywordss;




    private tp6_Researcher tp6_researcher;


    public tp6_Paper(
        String name    ) {
        this.name = name;
        this.tp6_researchers = new ArrayList<>();
        this.tp6_paperkeywordss = new ArrayList<>();
    }

    public tp6_Paper(
        String name        ArrayList<tp6_Researcher> tp6_researchers,        ArrayList<tp6_PaperKeywords> tp6_paperkeywordss    ) {
        this.name = name;
        this.tp6_researchers = tp6_researchers;
        this.tp6_paperkeywordss = tp6_paperkeywordss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tp6_PublicationStructure getTp6_publicationstructure() {
        return tp6_publicationstructure;
    }

    public void setTp6_publicationstructure(tp6_PublicationStructure tp6_publicationstructure) {
        this.tp6_publicationstructure = tp6_publicationstructure;
    }
    public List<tp6_Researcher> getTp6_researchers() {
        return tp6_researchers;
    }

    public void addTp6_researcher(Tp6_researcher tp6_researcher) {
        this.tp6_researchers.add(tp6_researcher);
    }
    public tp6_Paper getTp6_paper() {
        return tp6_paper;
    }

    public void setTp6_paper(tp6_Paper tp6_paper) {
        this.tp6_paper = tp6_paper;
    }
    public List<tp6_PaperKeywords> getTp6_paperkeywordss() {
        return tp6_paperkeywordss;
    }

    public void addTp6_paperkeywords(Tp6_paperkeywords tp6_paperkeywords) {
        this.tp6_paperkeywordss.add(tp6_paperkeywords);
    }
    public tp6_Researcher getTp6_researcher() {
        return tp6_researcher;
    }

    public void setTp6_researcher(tp6_Researcher tp6_researcher) {
        this.tp6_researcher = tp6_researcher;
    }

}