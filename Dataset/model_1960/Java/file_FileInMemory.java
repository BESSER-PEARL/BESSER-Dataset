





import java.util.List;
import java.util.ArrayList;

public class file_FileInMemory extends File {

    private String Content;



    public file_FileInMemory(
        String Content    ) {
        super(
        );
        this.Content = Content;
    }


    public String getContent() {
        return Content;
    }

    public void setContent(String Content) {
        this.Content = Content;
    }


}