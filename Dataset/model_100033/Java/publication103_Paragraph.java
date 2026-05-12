





import java.util.List;
import java.util.ArrayList;

public class publication103_Paragraph extends Named, Counted {

    private String content;





    private publication103_Write publication103_write;


    public publication103_Paragraph(
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

    public publication103_Write getPublication103_write() {
        return publication103_write;
    }

    public void setPublication103_write(publication103_Write publication103_write) {
        this.publication103_write = publication103_write;
    }

}