





import java.util.List;
import java.util.ArrayList;

public class tp6_Paragraph  {

    private String content;
    private int id;
    private String name;



    public tp6_Paragraph(
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


}