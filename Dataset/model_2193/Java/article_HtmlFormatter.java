





import java.util.List;
import java.util.ArrayList;

public class article_HtmlFormatter extends Formatter {

    private String file;



    public article_HtmlFormatter(
        String file    ) {
        super(
        );
        this.file = file;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }


}