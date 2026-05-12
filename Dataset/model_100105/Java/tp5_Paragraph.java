





import java.util.List;
import java.util.ArrayList;

public class tp5_Paragraph  {

    private String content;
    private int id;
    private String name;





    private tp5_Paper tp5_paper;


    public tp5_Paragraph(
        String content,        int id,        String name    ) {
        this.content = content;
        this.id = id;
        this.name = name;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tp5_Paper getTp5_paper() {
        return tp5_paper;
    }

    public void setTp5_paper(tp5_Paper tp5_paper) {
        this.tp5_paper = tp5_paper;
    }

}