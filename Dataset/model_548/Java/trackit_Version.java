





import java.util.List;
import java.util.ArrayList;

public class trackit_Version extends Identifiable {

    private String name;
    private String status;



    public trackit_Version(
        String name,        String status    ) {
        super(
        );
        this.name = name;
        this.status = status;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}