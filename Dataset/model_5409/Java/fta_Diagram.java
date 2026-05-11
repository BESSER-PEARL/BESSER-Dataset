





import java.util.List;
import java.util.ArrayList;

public class fta_Diagram  {

    private String detail;
    private String id;
    private String name;



    public fta_Diagram(
        String detail,        String id,        String name    ) {
        this.detail = detail;
        this.id = id;
        this.name = name;
    }


    public String getDetail() {
        return detail;
    }

    public void setDetail(String detail) {
        this.detail = detail;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}