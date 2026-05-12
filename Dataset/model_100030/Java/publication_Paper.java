





import java.util.List;
import java.util.ArrayList;

public class publication_Paper extends Named {






    private List<publication_Paragraph> publication_paragraphs;


    public publication_Paper(
    ) {
        super(
        );
        this.publication_paragraphs = new ArrayList<>();
    }

    public publication_Paper(
        ArrayList<publication_Paragraph> publication_paragraphs    ) {
        this.publication_paragraphs = publication_paragraphs;
    }


    public List<publication_Paragraph> getPublication_paragraphs() {
        return publication_paragraphs;
    }

    public void addPublication_paragraph(Publication_paragraph publication_paragraph) {
        this.publication_paragraphs.add(publication_paragraph);
    }

}