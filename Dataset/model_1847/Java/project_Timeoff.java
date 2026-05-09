





import java.util.List;
import java.util.ArrayList;

public class project_Timeoff extends NikuReportAttribute {

    private String id;
    private String name;



    public project_Timeoff(
        String id,        String name    ) {
        super(
        );
        this.id = id;
        this.name = name;
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