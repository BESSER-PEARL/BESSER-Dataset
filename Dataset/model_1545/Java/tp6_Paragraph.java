





import java.util.List;
import java.util.ArrayList;

public class tp6_Paragraph  {

    private String name;
    private int id;
    private String content;





    private tp6_Paper tp6_paper;


    public tp6_Paragraph(
        String name,        int id,        String content    ) {
        this.name = name;
        this.id = id;
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
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public tp6_Paper getTp6_paper() {
        return tp6_paper;
    }

    public void setTp6_paper(tp6_Paper tp6_paper) {
        this.tp6_paper = tp6_paper;
    }

}