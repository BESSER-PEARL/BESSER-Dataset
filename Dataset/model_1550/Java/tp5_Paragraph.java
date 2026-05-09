





import java.util.List;
import java.util.ArrayList;

public class tp5_Paragraph  {

    private String content;
    private String name;
    private int id;





    private tp5_Paper tp5_paper;


    public tp5_Paragraph(
        String content,        String name,        int id    ) {
        this.content = content;
        this.name = name;
        this.id = id;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public tp5_Paper getTp5_paper() {
        return tp5_paper;
    }

    public void setTp5_paper(tp5_Paper tp5_paper) {
        this.tp5_paper = tp5_paper;
    }

}