





import java.util.List;
import java.util.ArrayList;

public class Problem  {

    private String Id;
    private String Type;
    private String Content;



    public Problem(
        String Id,        String Type,        String Content    ) {
        this.Id = Id;
        this.Type = Type;
        this.Content = Content;
    }


    public String getId() {
        return Id;
    }

    public void setId(String Id) {
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


}