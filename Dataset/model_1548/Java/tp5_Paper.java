





import java.util.List;
import java.util.ArrayList;

public class tp5_Paper  {

    private String name;





    private tp5_Collaboration tp5_collaboration;




    private tp5_Researcher tp5_researcher;




    private tp5_Paper tp5_paper;




    private tp5_PublicationStructure tp5_publicationstructure;




    private List<tp5_Researcher> tp5_researchers;




    private List<tp5_Paragraph> tp5_paragraphs;


    public tp5_Paper(
        String name    ) {
        this.name = name;
        this.tp5_researchers = new ArrayList<>();
        this.tp5_paragraphs = new ArrayList<>();
    }

    public tp5_Paper(
        String name        ArrayList<tp5_Researcher> tp5_researchers,        ArrayList<tp5_Paragraph> tp5_paragraphs    ) {
        this.name = name;
        this.tp5_researchers = tp5_researchers;
        this.tp5_paragraphs = tp5_paragraphs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tp5_Collaboration getTp5_collaboration() {
        return tp5_collaboration;
    }

    public void setTp5_collaboration(tp5_Collaboration tp5_collaboration) {
        this.tp5_collaboration = tp5_collaboration;
    }
    public tp5_Researcher getTp5_researcher() {
        return tp5_researcher;
    }

    public void setTp5_researcher(tp5_Researcher tp5_researcher) {
        this.tp5_researcher = tp5_researcher;
    }
    public tp5_Paper getTp5_paper() {
        return tp5_paper;
    }

    public void setTp5_paper(tp5_Paper tp5_paper) {
        this.tp5_paper = tp5_paper;
    }
    public tp5_PublicationStructure getTp5_publicationstructure() {
        return tp5_publicationstructure;
    }

    public void setTp5_publicationstructure(tp5_PublicationStructure tp5_publicationstructure) {
        this.tp5_publicationstructure = tp5_publicationstructure;
    }
    public List<tp5_Researcher> getTp5_researchers() {
        return tp5_researchers;
    }

    public void addTp5_researcher(Tp5_researcher tp5_researcher) {
        this.tp5_researchers.add(tp5_researcher);
    }
    public List<tp5_Paragraph> getTp5_paragraphs() {
        return tp5_paragraphs;
    }

    public void addTp5_paragraph(Tp5_paragraph tp5_paragraph) {
        this.tp5_paragraphs.add(tp5_paragraph);
    }

}