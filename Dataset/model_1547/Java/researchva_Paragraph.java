





import java.util.List;
import java.util.ArrayList;

public class researchva_Paragraph extends Named, Counted {

    private String content;





    private researchva_Paper researchva_paper;




    private researchva_Write researchva_write;




    private List<researchva_ReviewNote> researchva_reviewnotes;


    public researchva_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.researchva_reviewnotes = new ArrayList<>();
    }

    public researchva_Paragraph(
        String content        ArrayList<researchva_ReviewNote> researchva_reviewnotes    ) {
        this.content = content;
        this.researchva_reviewnotes = researchva_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public researchva_Paper getResearchva_paper() {
        return researchva_paper;
    }

    public void setResearchva_paper(researchva_Paper researchva_paper) {
        this.researchva_paper = researchva_paper;
    }
    public researchva_Write getResearchva_write() {
        return researchva_write;
    }

    public void setResearchva_write(researchva_Write researchva_write) {
        this.researchva_write = researchva_write;
    }
    public List<researchva_ReviewNote> getResearchva_reviewnotes() {
        return researchva_reviewnotes;
    }

    public void addResearchva_reviewnote(Researchva_reviewnote researchva_reviewnote) {
        this.researchva_reviewnotes.add(researchva_reviewnote);
    }

}