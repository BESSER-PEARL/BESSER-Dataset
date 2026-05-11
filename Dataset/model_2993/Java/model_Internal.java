





import java.util.List;
import java.util.ArrayList;

public class model_Internal extends Content {

    private String content;
    private String typePrefix;



    public model_Internal(
        String content,        String typePrefix    ) {
        super(
        );
        this.content = content;
        this.typePrefix = typePrefix;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getTypeprefix() {
        return typePrefix;
    }

    public void setTypeprefix(String typePrefix) {
        this.typePrefix = typePrefix;
    }


}