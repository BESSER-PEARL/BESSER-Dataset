





import java.util.List;
import java.util.ArrayList;

public class Problem  {

    private String Type;
    private String Content;
    private String Id;



    public Problem(
        String Type,        String Content,        String Id    ) {
        this.Type = Type;
        this.Content = Content;
        this.Id = Id;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getContent() {
        return Content;
    }

    public void setContent(String Content) {
        this.Content = Content;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }


}