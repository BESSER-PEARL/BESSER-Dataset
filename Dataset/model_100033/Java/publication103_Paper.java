





import java.util.List;
import java.util.ArrayList;

public class publication103_Paper extends Named {






    private publication103_Researcher publication103_researcher;




    private List<publication103_Paragraph> publication103_paragraphs;




    private List<publication103_Researcher> publication103_researchers;




    private publication103_Paper publication103_paper;


    public publication103_Paper(
    ) {
        super(
        );
        this.publication103_paragraphs = new ArrayList<>();
        this.publication103_researchers = new ArrayList<>();
    }

    public publication103_Paper(
        ArrayList<publication103_Paragraph> publication103_paragraphs,        ArrayList<publication103_Researcher> publication103_researchers    ) {
        this.publication103_paragraphs = publication103_paragraphs;
        this.publication103_researchers = publication103_researchers;
    }


    public publication103_Researcher getPublication103_researcher() {
        return publication103_researcher;
    }

    public void setPublication103_researcher(publication103_Researcher publication103_researcher) {
        this.publication103_researcher = publication103_researcher;
    }
    public List<publication103_Paragraph> getPublication103_paragraphs() {
        return publication103_paragraphs;
    }

    public void addPublication103_paragraph(Publication103_paragraph publication103_paragraph) {
        this.publication103_paragraphs.add(publication103_paragraph);
    }
    public List<publication103_Researcher> getPublication103_researchers() {
        return publication103_researchers;
    }

    public void addPublication103_researcher(Publication103_researcher publication103_researcher) {
        this.publication103_researchers.add(publication103_researcher);
    }
    public publication103_Paper getPublication103_paper() {
        return publication103_paper;
    }

    public void setPublication103_paper(publication103_Paper publication103_paper) {
        this.publication103_paper = publication103_paper;
    }

}