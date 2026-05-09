





import java.util.List;
import java.util.ArrayList;

public class tp4_Paper extends Named {






    private List<tp4_Keyword> tp4_keywords;




    private List<tp4_Paragraph> tp4_paragraphs;


    public tp4_Paper(
    ) {
        super(
        );
        this.tp4_keywords = new ArrayList<>();
        this.tp4_paragraphs = new ArrayList<>();
    }

    public tp4_Paper(
        ArrayList<tp4_Keyword> tp4_keywords,        ArrayList<tp4_Paragraph> tp4_paragraphs    ) {
        this.tp4_keywords = tp4_keywords;
        this.tp4_paragraphs = tp4_paragraphs;
    }


    public List<tp4_Keyword> getTp4_keywords() {
        return tp4_keywords;
    }

    public void addTp4_keyword(Tp4_keyword tp4_keyword) {
        this.tp4_keywords.add(tp4_keyword);
    }
    public List<tp4_Paragraph> getTp4_paragraphs() {
        return tp4_paragraphs;
    }

    public void addTp4_paragraph(Tp4_paragraph tp4_paragraph) {
        this.tp4_paragraphs.add(tp4_paragraph);
    }

}