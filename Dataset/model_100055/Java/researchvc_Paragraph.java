





import java.util.List;
import java.util.ArrayList;

public class researchvc_Paragraph extends Named, Counted {

    private String content;





    private researchvc_Write researchvc_write;




    private researchvc_Paper researchvc_paper;


    public researchvc_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public researchvc_Write getResearchvc_write() {
        return researchvc_write;
    }

    public void setResearchvc_write(researchvc_Write researchvc_write) {
        this.researchvc_write = researchvc_write;
    }
    public researchvc_Paper getResearchvc_paper() {
        return researchvc_paper;
    }

    public void setResearchvc_paper(researchvc_Paper researchvc_paper) {
        this.researchvc_paper = researchvc_paper;
    }

}