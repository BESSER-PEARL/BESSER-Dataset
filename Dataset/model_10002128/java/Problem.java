





import java.util.List;
import java.util.ArrayList;

public class Problem  {

    private String Content;
    private String Type;
    private String Id;



    public Problem(
        String Content,        String Type,        String Id    ) {
        this.Content = Content;
        this.Type = Type;
        this.Id = Id;
    }


    public String getContent() {
        return Content;
    }

    public void setContent(String Content) {
        this.Content = Content;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }


}