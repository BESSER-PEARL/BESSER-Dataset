





import java.util.List;
import java.util.ArrayList;

public class restapp_model_Category  {

    private String description;
    private int status;
    private String name;
    private int id;



    public restapp_model_Category(
        String description,        int status,        String name,        int id    ) {
        this.description = description;
        this.status = status;
        this.name = name;
        this.id = id;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}