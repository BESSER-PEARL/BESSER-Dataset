





import java.util.List;
import java.util.ArrayList;

public class tp6_Paragraph  {

    private int id;
    private String content;
    private String name;



    public tp6_Paragraph(
        int id,        String content,        String name    ) {
        this.id = id;
        this.content = content;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}