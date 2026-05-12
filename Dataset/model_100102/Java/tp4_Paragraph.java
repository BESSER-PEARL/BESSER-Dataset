





import java.util.List;
import java.util.ArrayList;

public class tp4_Paragraph extends Named, Counted {

    private String content;





    private tp4_Paper tp4_paper;




    private tp4_Write tp4_write;


    public tp4_Paragraph(
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

    public tp4_Paper getTp4_paper() {
        return tp4_paper;
    }

    public void setTp4_paper(tp4_Paper tp4_paper) {
        this.tp4_paper = tp4_paper;
    }
    public tp4_Write getTp4_write() {
        return tp4_write;
    }

    public void setTp4_write(tp4_Write tp4_write) {
        this.tp4_write = tp4_write;
    }

}