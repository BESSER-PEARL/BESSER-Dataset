





import java.util.List;
import java.util.ArrayList;

public class courses_Paragraph  {

    private String name;
    private String description;





    private courses_Content courses_content;


    public courses_Paragraph(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public courses_Content getCourses_content() {
        return courses_content;
    }

    public void setCourses_content(courses_Content courses_content) {
        this.courses_content = courses_content;
    }

}