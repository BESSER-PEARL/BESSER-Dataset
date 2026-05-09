





import java.util.List;
import java.util.ArrayList;

public class publication101_Paper extends Named {






    private publication101_Collaboration publication101_collaboration;




    private List<publication101_Paragraph> publication101_paragraphs;




    private publication101_Paper publication101_paper;


    public publication101_Paper(
    ) {
        super(
        );
        this.publication101_paragraphs = new ArrayList<>();
    }

    public publication101_Paper(
        ArrayList<publication101_Paragraph> publication101_paragraphs    ) {
        this.publication101_paragraphs = publication101_paragraphs;
    }


    public publication101_Collaboration getPublication101_collaboration() {
        return publication101_collaboration;
    }

    public void setPublication101_collaboration(publication101_Collaboration publication101_collaboration) {
        this.publication101_collaboration = publication101_collaboration;
    }
    public List<publication101_Paragraph> getPublication101_paragraphs() {
        return publication101_paragraphs;
    }

    public void addPublication101_paragraph(Publication101_paragraph publication101_paragraph) {
        this.publication101_paragraphs.add(publication101_paragraph);
    }
    public publication101_Paper getPublication101_paper() {
        return publication101_paper;
    }

    public void setPublication101_paper(publication101_Paper publication101_paper) {
        this.publication101_paper = publication101_paper;
    }

}