





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_SelectSource extends SingleSource {

    private String name;



    public sqliteModel_SelectSource(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}