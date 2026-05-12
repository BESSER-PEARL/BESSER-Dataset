





import java.util.List;
import java.util.ArrayList;

public class opf_Meta  {

    private String content;
    private String name;





    private opf_Metadata opf_metadata;


    public opf_Meta(
        String content,        String name    ) {
        this.content = content;
        this.name = name;
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

    public opf_Metadata getOpf_metadata() {
        return opf_metadata;
    }

    public void setOpf_metadata(opf_Metadata opf_metadata) {
        this.opf_metadata = opf_metadata;
    }

}