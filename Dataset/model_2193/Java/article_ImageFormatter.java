





import java.util.List;
import java.util.ArrayList;

public class article_ImageFormatter extends Formatter {

    private String file;



    public article_ImageFormatter(
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