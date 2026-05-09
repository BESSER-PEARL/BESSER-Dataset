





import java.util.List;
import java.util.ArrayList;

public class bz288963_Book  {

    private String selfdef;
    private String type;
    private String id;





    private bz288963_Book bz288963_book;




    private List<bz288963_Paragraph> bz288963_paragraphs;


    public bz288963_Book(
        String selfdef,        String type,        String id    ) {
        this.selfdef = selfdef;
        this.type = type;
        this.id = id;
        this.bz288963_paragraphs = new ArrayList<>();
    }

    public bz288963_Book(
        String selfdef,        String type,        String id        ArrayList<bz288963_Paragraph> bz288963_paragraphs    ) {
        this.selfdef = selfdef;
        this.type = type;
        this.id = id;
        this.bz288963_paragraphs = bz288963_paragraphs;
    }

    public String getSelfdef() {
        return selfdef;
    }

    public void setSelfdef(String selfdef) {
        this.selfdef = selfdef;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public bz288963_Book getBz288963_book() {
        return bz288963_book;
    }

    public void setBz288963_book(bz288963_Book bz288963_book) {
        this.bz288963_book = bz288963_book;
    }
    public List<bz288963_Paragraph> getBz288963_paragraphs() {
        return bz288963_paragraphs;
    }

    public void addBz288963_paragraph(Bz288963_paragraph bz288963_paragraph) {
        this.bz288963_paragraphs.add(bz288963_paragraph);
    }

}