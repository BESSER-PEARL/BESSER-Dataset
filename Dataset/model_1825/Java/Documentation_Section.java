





import java.util.List;
import java.util.ArrayList;

public class Documentation_Section  {

    private String title;





    private Documentation_Book documentation_book;




    private Documentation_XRefValue documentation_xrefvalue;




    private Documentation_Section documentation_section;




    private List<Documentation_Paragraph> documentation_paragraphs;


    public Documentation_Section(
        String title    ) {
        this.title = title;
        this.documentation_paragraphs = new ArrayList<>();
    }

    public Documentation_Section(
        String title        ArrayList<Documentation_Paragraph> documentation_paragraphs    ) {
        this.title = title;
        this.documentation_paragraphs = documentation_paragraphs;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Documentation_Book getDocumentation_book() {
        return documentation_book;
    }

    public void setDocumentation_book(Documentation_Book documentation_book) {
        this.documentation_book = documentation_book;
    }
    public Documentation_XRefValue getDocumentation_xrefvalue() {
        return documentation_xrefvalue;
    }

    public void setDocumentation_xrefvalue(Documentation_XRefValue documentation_xrefvalue) {
        this.documentation_xrefvalue = documentation_xrefvalue;
    }
    public Documentation_Section getDocumentation_section() {
        return documentation_section;
    }

    public void setDocumentation_section(Documentation_Section documentation_section) {
        this.documentation_section = documentation_section;
    }
    public List<Documentation_Paragraph> getDocumentation_paragraphs() {
        return documentation_paragraphs;
    }

    public void addDocumentation_paragraph(Documentation_paragraph documentation_paragraph) {
        this.documentation_paragraphs.add(documentation_paragraph);
    }

}