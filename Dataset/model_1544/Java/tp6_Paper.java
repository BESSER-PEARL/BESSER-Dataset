





import java.util.List;
import java.util.ArrayList;

public class tp6_Paper  {

    private String name;





    private tp6_Researcher tp6_researcher;




    private tp6_Collaboration tp6_collaboration;




    private List<tp6_Paragraph> tp6_paragraphs;




    private tp6_Paper tp6_paper;




    private List<tp6_Researcher> tp6_researchers;


    public tp6_Paper(
        String name    ) {
        this.name = name;
        this.tp6_paragraphs = new ArrayList<>();
        this.tp6_researchers = new ArrayList<>();
    }

    public tp6_Paper(
        String name        ArrayList<tp6_Paragraph> tp6_paragraphs,        ArrayList<tp6_Researcher> tp6_researchers    ) {
        this.name = name;
        this.tp6_paragraphs = tp6_paragraphs;
        this.tp6_researchers = tp6_researchers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tp6_Researcher getTp6_researcher() {
        return tp6_researcher;
    }

    public void setTp6_researcher(tp6_Researcher tp6_researcher) {
        this.tp6_researcher = tp6_researcher;
    }
    public tp6_Collaboration getTp6_collaboration() {
        return tp6_collaboration;
    }

    public void setTp6_collaboration(tp6_Collaboration tp6_collaboration) {
        this.tp6_collaboration = tp6_collaboration;
    }
    public List<tp6_Paragraph> getTp6_paragraphs() {
        return tp6_paragraphs;
    }

    public void addTp6_paragraph(Tp6_paragraph tp6_paragraph) {
        this.tp6_paragraphs.add(tp6_paragraph);
    }
    public tp6_Paper getTp6_paper() {
        return tp6_paper;
    }

    public void setTp6_paper(tp6_Paper tp6_paper) {
        this.tp6_paper = tp6_paper;
    }
    public List<tp6_Researcher> getTp6_researchers() {
        return tp6_researchers;
    }

    public void addTp6_researcher(Tp6_researcher tp6_researcher) {
        this.tp6_researchers.add(tp6_researcher);
    }

}