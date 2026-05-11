





import java.util.List;
import java.util.ArrayList;

public class extended_Page extends AbstractElement {

    private String title;
    private String header;
    private String footer;
    private String name;



    public extended_Page(
        String title,        String header,        String footer,        String name    ) {
        super(
        );
        this.title = title;
        this.header = header;
        this.footer = footer;
        this.name = name;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getHeader() {
        return header;
    }

    public void setHeader(String header) {
        this.header = header;
    }
    public String getFooter() {
        return footer;
    }

    public void setFooter(String footer) {
        this.footer = footer;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}