





import java.util.List;
import java.util.ArrayList;

public class publication2014_Paper extends Named {






    private List<publication2014_Researcher> publication2014_researchers;




    private List<publication2014_Paragraph> publication2014_paragraphs;




    private publication2014_Researcher publication2014_researcher;


    public publication2014_Paper(
    ) {
        super(
        );
        this.publication2014_researchers = new ArrayList<>();
        this.publication2014_paragraphs = new ArrayList<>();
    }

    public publication2014_Paper(
        ArrayList<publication2014_Researcher> publication2014_researchers,        ArrayList<publication2014_Paragraph> publication2014_paragraphs    ) {
        this.publication2014_researchers = publication2014_researchers;
        this.publication2014_paragraphs = publication2014_paragraphs;
    }


    public List<publication2014_Researcher> getPublication2014_researchers() {
        return publication2014_researchers;
    }

    public void addPublication2014_researcher(Publication2014_researcher publication2014_researcher) {
        this.publication2014_researchers.add(publication2014_researcher);
    }
    public List<publication2014_Paragraph> getPublication2014_paragraphs() {
        return publication2014_paragraphs;
    }

    public void addPublication2014_paragraph(Publication2014_paragraph publication2014_paragraph) {
        this.publication2014_paragraphs.add(publication2014_paragraph);
    }
    public publication2014_Researcher getPublication2014_researcher() {
        return publication2014_researcher;
    }

    public void setPublication2014_researcher(publication2014_Researcher publication2014_researcher) {
        this.publication2014_researcher = publication2014_researcher;
    }

}