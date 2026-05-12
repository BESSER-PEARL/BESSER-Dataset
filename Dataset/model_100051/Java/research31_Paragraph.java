





import java.util.List;
import java.util.ArrayList;

public class research31_Paragraph extends Counted, Named {

    private String content;





    private research31_Write research31_write;


    public research31_Paragraph(
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

    public research31_Write getResearch31_write() {
        return research31_write;
    }

    public void setResearch31_write(research31_Write research31_write) {
        this.research31_write = research31_write;
    }

}