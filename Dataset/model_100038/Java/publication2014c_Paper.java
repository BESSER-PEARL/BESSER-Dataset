





import java.util.List;
import java.util.ArrayList;

public class publication2014c_Paper extends Named {






    private List<publication2014c_Paragraph> publication2014c_paragraphs;




    private publication2014c_PublicationStructure publication2014c_publicationstructure;


    public publication2014c_Paper(
    ) {
        super(
        );
        this.publication2014c_paragraphs = new ArrayList<>();
    }

    public publication2014c_Paper(
        ArrayList<publication2014c_Paragraph> publication2014c_paragraphs    ) {
        this.publication2014c_paragraphs = publication2014c_paragraphs;
    }


    public List<publication2014c_Paragraph> getPublication2014c_paragraphs() {
        return publication2014c_paragraphs;
    }

    public void addPublication2014c_paragraph(Publication2014c_paragraph publication2014c_paragraph) {
        this.publication2014c_paragraphs.add(publication2014c_paragraph);
    }
    public publication2014c_PublicationStructure getPublication2014c_publicationstructure() {
        return publication2014c_publicationstructure;
    }

    public void setPublication2014c_publicationstructure(publication2014c_PublicationStructure publication2014c_publicationstructure) {
        this.publication2014c_publicationstructure = publication2014c_publicationstructure;
    }

}